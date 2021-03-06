Summary: The Webber tool used in RedIRIS to produce nice HTML web pages
Name: webber
Version: 3.0.RC1.Beta.Epsilon
Release: 1 
License: BSD license 
Group: System Environment/Tools
#Source: %{name}-%{version}.tar.gz
Source: webber.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Packager: Webbon <webbones@rediris.es>
BuildArch: noarch
Requires:  perl-HTML-Parser perl-XML-Parser
%description

This is the webber tool used to produce static HTML pages, from snippets of it,
appling the same template to produce nice pages without needing to repeat most
of the information.

You can think in webber, as "Make on Steroid" mixed with Drupal ;-)


%package mod_perl
Summary:       Webber module for use with Mod_Perl2
Group:         System Environment/Daemons
Requires:      webber = %{version}-%{release}
%description mod_perl

Configuration files and support for using Webber with Apache2 and mod_perl2,
so it can produce HTML pages dinamically.


%prep
%setup -q -n webber3

%build
echo "Currently there is no build, it's only Perl code"

%install 

#cd trunk 
ROOT=$RPM_BUILD_ROOT make install_webber
ROOT=$RPM_BUILD_ROOT make install_apache 

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/share/doc/webber/readme
/usr/share/doc/webber/leeme
/usr/bin/webber
/usr/lib/webber/proc/PrintIn.pm
/usr/lib/webber/proc/Slide.pm
/usr/lib/webber/proc/Caparse.pm
/usr/lib/webber/proc/Mediwiki.pm
/usr/lib/webber/proc/Exec.pm
/usr/lib/webber/proc/FileLang.pm
/usr/lib/webber/proc/Maketoc.pm
/usr/lib/webber/proc/Encoder.pm
/usr/lib/webber/proc/BodyFaq.pm
/usr/lib/webber/proc/PgpSign.pm
/usr/lib/webber/proc/CopyFiles.pm
/usr/lib/webber/proc/Macros.pm
/usr/lib/webber/proc/Webbo.pm
/usr/lib/webber/proc/DumpVars.pm
/usr/lib/webber/proc/Capaweb.pm
/usr/lib/webber/proc/Vars.pm
/usr/lib/webber/proc/Menu.pm
/usr/lib/webber/proc/Table.pm
/etc/webber/webber.wbb
/var/log/webber
/etc/logrotate.d/webber.logrotate
/usr/lib/webber/proc/ExtraProc.pm
/usr/lib/webber/proc/File.pm

%files mod_perl
/etc/httpd/conf.d/webber.conf
/etc/webber/apache-config.xml
/usr/lib/perl5/5.8.8/Webber/FilterHTML.pm
/usr/lib/perl5/5.8.8/Webber/FilterRaw.pm
/usr/lib/perl5/5.8.8/Webber/startup.pl
/usr/share/doc/webber/readme-modperl2.txt
/var/www/html/webber/hello.php
/var/www/html/webber/hello.wbb
%changelog



