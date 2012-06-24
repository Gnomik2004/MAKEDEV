Summary:	Program to make and update /dev entries
Summary(de):	Script zum Erstellen und Aktualisieren von /dev-Eintr�gen
Summary(es):	Script para hacer y actualizar entradas referentes a dispositivos en /dev
Summary(fr):	Script pour cr�er et mettre � jour les entr�es /dev
Summary(pl):	Program do tworzenia i poprawiania urz�dze� z /dev
Summary(pt_BR):	Script para fazer e atualizar entradas referentes a dispositivos em /dev
Summary(tr):	Ayg�t tan�m� yapmak ve de�i�tirmek i�in bir ara�
Name:		MAKEDEV
Version:	3.13
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	%{name}-%{version}-1.tar.gz
# Source0-md5:	f8befaebd0813c6fa59c07ef3875f232
Patch0:		%{name}-ub.patch
BuildRequires:	libselinux-devel >= 0:1.8
Requires:	libselinux >= 0:1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/sbin

%description
The /dev tree holds special files, each of which corresponds to a type
of hardware device that Linux supports. This package contains a
program which makes it easier to create and maintain the files which
fill the /dev tree.

%description -l de
Die /dev-Hierarchie enth�lt spezielle Dateien, von denen jede einem
Hardwareger�ttyp entspricht, der von Linux unterst�tzt wird. Dieses
Paket enth�lt ein Skript, das die Erstellung und die Pflege der
Dateien innerhalb dieser Hierarchie vereinfacht.

%description -l es
El directorio /dev posee archivos especiales, cada uno de ellos
correspondiendo a un tipo de dispositivo de hardware que Linux
soporta. Este paquete contiene un script que hace m�s f�cil la
creaci�n y manutenci�n de los archivos en el directorio /dev.

%description -l fr
L'arborescence /dev contient des fichiers sp�ciaux. Chacun d'eux
correspond � un p�riph�rique mat�riel g�rable par Linux. Ce paquetage
contient un script facilitant la cr�ation et la maintenance des
fichiers qui remplissent l'arborescence /dev.

%description -l pl
Pliki specjalne znajduj�ce si� w katalogu /dev odpowiadaj�
urz�dzeniom, kt�re s� obs�ugiwane przez Linuksa. Pakiet ten zawiera
program, kt�ry uczyni tworzenie i operowanie tymi plikami �atwiejszym.

%description -l pt_BR
O diret�rio /dev possui arquivos especiais, cada um deles
correspondendo a um tipo de dispositivo de hardware que o Linux
suporta. Este pacote cont�m um script que torna mais f�cil a cria��o
e manuten��o dos arquivos no diret�rio /dev.

%description -l tr
Unix ve Unix benzeri sistemler (Linux da dahil olmak �zere), makinaya
ba�l� ayg�tlar� g�stermek i�in �zel dosyalar kullan�rlar. Bu �zel
dosyalar�n t�m� /dev dizin yap�s� alt�ndad�r. Bu paket en �ok
kullan�lan /dev dosyalar�n� i�erir. Bu dosyalar, bir sistemin d�zg�n
olarak i�leyebilmesi i�in temel gereksinimlerdendir.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags} %{rpmldflags}" \
	SELINUX=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	devdir=/dev \
	makedevdir=/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/MAKEDEV
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%config %{_sysconfdir}/makedev.d
