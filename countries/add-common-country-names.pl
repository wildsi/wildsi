#!/usr/bin/perl
use strict;
use warnings;
use utf8;

use JSON::MaybeXS;
use Text::CSV;
use open qw( :encoding(UTF-8) :std );
binmode(STDOUT, ":utf8");

# This is a simple script for mapping common country names to a file with ISO codes
# using the JSON country data distributed by mledoze at https://github.com/mledoze/countries

# Configure
my $iso_column = 7;  # Tell the script in which column to expect the two letter ISO codes
my $name_column = 6; # Tell the scrript in which column to expect default names
my $skip_header = 1; # If true this assumes the first line is a header row

# Data
my %common_names;    # two-letter ISO code -> common name
my %independent;     # two-letter ISO code -> 1/undef

# Get input file from user
my $usage = "Please provide paths to the country CSV file that you want to annotate with 
common names and a JSON file with the names.\n\n$0 country.csv countries.json";

unless ( $ARGV[0] && $ARGV[1] ) { die "\n$usage\n\n" }

# Read the json file
my $json_text = do {
   open(my $json_fh, "<:encoding(UTF-8)", $ARGV[1])
      or die("Can't open \"$ARGV[1]\": $!\n");
   local $/;
   <$json_fh>
};

my $json = JSON()->new;
my $data = $json->decode($json_text);

foreach ( @{$data} ) {
	if ( $_->{cca2} && $_->{name}->{common} ) {
		$common_names{$_->{cca2}} = $_->{name}->{common};
	}
	if ( $_->{cca2} && $_->{independent} && $_->{independent} eq 'true' ) {
		$independent{$_->{cca2}} = 1;
	}
}

# Read and annotate the country.csv file
my $csv = Text::CSV->new ({ binary => 1, auto_diag => 1 });
open my $fh, "<:encoding(utf8)", $ARGV[0] or die "$ARGV[0]: $!";

my @rows;
my $line = 0; 
while (my $row = $csv->getline ($fh)) {
	++$line;
	if ( $line == 1 && $skip_header ) {
		push @$row, "SIMPLIFIED_NAME";
	} else {
		if ( $row->[$iso_column] ne '' && $common_names{$row->[$iso_column]} ) {
			push @$row, $common_names{$row->[$iso_column]};
			unless ( $independent{$row->[$iso_column]} ) {
				print STDERR "Country $row->[$iso_column] is not an independent state.\n";
			}
		} else {
			if ( $row->[$name_column] ) {
				push @$row, $row->[$name_column];
				print STDERR "Country $row->[$name_column] cannot be mapped to a simplified name. Using default name.\n";
			}
		}
	}
	push @rows, $row
}

# and write as CSV
open $fh, ">:encoding(utf8)", "new.csv" or die "new.csv: $!";
$csv->say ($fh, $_) for @rows;
close $fh or die "new.csv: $!";	

exit;