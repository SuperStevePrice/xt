#!/usr/bin/env ksh

#-------------------------------------------------------------------------------
#         Copyright (C) 2023    Steve Price    SuperStevePrice@gmail.com
#
#                       GNU GENERAL PUBLIC LICENSE
#                        Version 3, 29 June 2007
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# PROGRAM:
#   tk_perl_tester.ksh	
#
# PURPOSE:
#	Test various Perl executables to see which support Tk, used by xt.pl.
#	
# USAGE:
#   tk_perl_tester.ksh
#-------------------------------------------------------------------------------

check_tk_support() { 
    perl_path=$1
    print $perl_path ~/tests/test_tk.pl
    $perl_path ~/tests/test_tk.pl
} # check_tk_support()

pp="/usr/bin/perl /usr/bin/perl5.30 /usr/bin/perl5.34"
pp="$pp /usr/local/bin/perl /opt/homebrew/bin/perl /opt/homebrew/bin/perl5.36.1"
perl_paths=$pp

for perl_path in $(print $perl_paths) 
do
    check_tk_support $perl_path 
    if [ $? -eq 0 ]
    then
        print "Perl executable $perl_path supports Tk"
     else
        print "Perl executable $perl_path does not support Tk"
    fi
    print
done
