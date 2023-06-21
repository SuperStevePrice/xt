#!/usr/bin/env ksh
<<<<<<< HEAD
if [ X"$(uname)" == X"Darwin" ]
then
    perl=/usr/local/bin/perl5.36.1
else
    perl=/usr/bin/perl5.34-x86_64-linux-gnu
fi
$perl ~/bin/xt.pl &
=======

/usr/bin/perl5.34-x86_64-linux-gnu ~/bin/xt.pl &
>>>>>>> cfb7eba7dba525634f99fcfdb6679c5528032a38
