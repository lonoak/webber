#!/usr/bin/perl
#
# Webber processor for creating HTML from media wiki
#


my $name=       "MediaWiki";
my $version=    "1.0";

package MediaWiki ;

#DEBUG-INSERT-START

#-------------------------------------------------------------------------
# Function: debug
# Version 2.0
# Permite el "debug por niveles independientes"
 
#-------------------------------------------------------------------------
sub debug {
        my @lines = @_ ;
# Por el tema de strict 
        no strict "subs" ;
	my $level = $lines[0] ;
	unshift @lines , $name;
        if (defined main::debug_print) { main::debug_print (@lines) ; }
       else {
          my $level = shift @lines ;
        my $line= join '', @lines ;
        chomp $line ;
        print STDERR "$name: $line\n" ;
        }
use strict "subs" ;
# Joder mierda del strict 
}
# End Funcion debug



#DEBUG-INSERT-END







my %defs = (
	'mediawiki.vars' => 'wbbOut:wbbOut wbbIn:wbbIn' ,
	) ;

sub info {
   print "$name v$version:  TRranform a wbb Var from MediaWiki to HTML \n";
}

sub help
{
   print <<FINAL
$name 

Webber processor, version $version
This program must run inside Webber.
This processor modified the a list of webber vars , changing the mediawiki 
to  XHTML 

$name can be used in any list of processors

$name uses the following Webber variables:
 #mediawiki.vars : vars to change
 defaults to $defs{'mediawiki.vars'} 

format varsource:vardestination

FINAL
}

sub mediawiki
{
#  use XHTML::MediaWiki;
  my $mediawiki = XHTML::MediaWiki->new();

   debug( 1, "(MediaWiki) MediaWiki  se ejecuta\n") ;
   my $rv =$_[0] ;
	
  $vars = defined ($$rv{'mediawiki.vars'}) ? $$rv{'mediawiki.vars'} : $defs{'mediawiki.vars'} ;

  foreach my $do  (split /\s+/, $vars)  {
	my ($src,$dst) = split /:/ , $do ;
	$$rv{$dst} = $mediawiki->format ($$rv{$src} ) ;
 }
}

if ($0 =~ /$name/) { &help; die ("\n"); }

1;
