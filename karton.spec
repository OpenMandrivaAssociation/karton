%define date 20250617

Name:		karton
Version:	0.0.0%{?date:~%{date}}
Release:	1
Source0:	https://invent.kde.org/sitter/karton/-/archive/master/karton-master.tar.bz2#/%{name}-%{version}.tar.bz2
Summary:	A libvirt based virtual machine manager
URL:		https://invent.kde.org/sitter/karton/
License:	GPL-3.0 and BSD-2-Clause and CC-BY-SA-4.0 and CC0-1.0
Group:		System
BuildRequires:	pkgconfig(libvirt)
BuildRequires:	pkgconfig(libosinfo-1.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	cmake(KF6Kirigami)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6QQC2DesktopStyle)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	qml(org.kde.kirigami)
BuildRequires:	cmake(Qt6CorePrivate)
BuildRequires:	cmake(Qt6QmlIntegrationPrivate)
BuildRequires:	cmake(Qt6NetworkPrivate)
BuildRequires:	cmake(Qt6QmlPrivate)
BuildRequires:	cmake(Qt6ConcurrentPrivate)
BuildRequires:	cmake(Qt6QmlAssetDownloaderPrivate)
BuildRequires:	cmake(Qt6DBusTools)
BuildRequires:	cmake(Qt6DBusPrivate)
BuildRequires:	cmake(Qt6GuiPrivate)
BuildRequires:	cmake(Qt6QmlModelsPrivate)
BuildRequires:	cmake(Qt6QmlWorkerScriptPrivate)
BuildRequires:	cmake(Qt6QmlMetaPrivate)
BuildRequires:	cmake(Qt6OpenGLPrivate)
BuildRequires:	cmake(Qt6TestPrivate)
BuildRequires:	cmake(Qt6QuickTemplates2Private)
BuildRequires:	cmake(Qt6QuickControls2Private)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6WidgetsPrivate)
BuildRequires:	cmake(Qt6XmlPrivate)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QmlTools)
BuildRequires:	cmake(Qt6QuickTools)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6CoreTools)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6WidgetsTools)
BuildRequires:	gettext
BuildSystem:	cmake
Requires:	qml(org.kde.kirigami)

%description
A libvirt based virtual machine manager

%files
%{_bindir}/karton
%{_datadir}/applications/org.kde.karton.desktop
%{_datadir}/icons/hicolor/scalable/apps/karton_logo.png
%{_datadir}/qlogging-categories6/karton.categories
