"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceImageErrorDetailCode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces.errors import DeserializationError
from aws_sdk_workspaces._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

WorkspaceImageErrorDetailCode: TypeAlias = Literal[
    "OutdatedPowershellVersion",
    "OfficeInstalled",
    "PCoIPAgentInstalled",
    "WindowsUpdatesEnabled",
    "AutoMountDisabled",
    "WorkspacesBYOLAccountNotFound",
    "WorkspacesBYOLAccountDisabled",
    "DHCPDisabled",
    "DiskFreeSpace",
    "AdditionalDrivesAttached",
    "OSNotSupported",
    "DomainJoined",
    "AzureDomainJoined",
    "FirewallEnabled",
    "VMWareToolsInstalled",
    "DiskSizeExceeded",
    "IncompatiblePartitioning",
    "PendingReboot",
    "AutoLogonEnabled",
    "RealTimeUniversalDisabled",
    "MultipleBootPartition",
    "Requires64BitOS",
    "ZeroRearmCount",
    "InPlaceUpgrade",
    "AntiVirusInstalled",
    "UEFINotSupported",
    "UnknownError",
    "AppXPackagesInstalled",
    "ReservedStorageInUse",
    "AdditionalDrivesPresent",
    "WindowsUpdatesRequired",
    "SysPrepFileMissing",
    "UserProfileMissing",
    "InsufficientDiskSpace",
    "EnvironmentVariablesPathMissingEntries",
    "DomainAccountServicesFound",
    "InvalidIp",
    "RemoteDesktopServicesDisabled",
    "WindowsModulesInstallerDisabled",
    "AmazonSsmAgentEnabled",
    "UnsupportedSecurityProtocol",
    "MultipleUserProfiles",
    "StagedAppxPackage",
    "UnsupportedOsUpgrade",
    "InsufficientRearmCount",
    "ProtocolOSIncompatibility",
    "MemoryIntegrityIncompatibility",
    "RestrictedDriveLetterInUse",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OutdatedPowershellVersion",
        "OfficeInstalled",
        "PCoIPAgentInstalled",
        "WindowsUpdatesEnabled",
        "AutoMountDisabled",
        "WorkspacesBYOLAccountNotFound",
        "WorkspacesBYOLAccountDisabled",
        "DHCPDisabled",
        "DiskFreeSpace",
        "AdditionalDrivesAttached",
        "OSNotSupported",
        "DomainJoined",
        "AzureDomainJoined",
        "FirewallEnabled",
        "VMWareToolsInstalled",
        "DiskSizeExceeded",
        "IncompatiblePartitioning",
        "PendingReboot",
        "AutoLogonEnabled",
        "RealTimeUniversalDisabled",
        "MultipleBootPartition",
        "Requires64BitOS",
        "ZeroRearmCount",
        "InPlaceUpgrade",
        "AntiVirusInstalled",
        "UEFINotSupported",
        "UnknownError",
        "AppXPackagesInstalled",
        "ReservedStorageInUse",
        "AdditionalDrivesPresent",
        "WindowsUpdatesRequired",
        "SysPrepFileMissing",
        "UserProfileMissing",
        "InsufficientDiskSpace",
        "EnvironmentVariablesPathMissingEntries",
        "DomainAccountServicesFound",
        "InvalidIp",
        "RemoteDesktopServicesDisabled",
        "WindowsModulesInstallerDisabled",
        "AmazonSsmAgentEnabled",
        "UnsupportedSecurityProtocol",
        "MultipleUserProfiles",
        "StagedAppxPackage",
        "UnsupportedOsUpgrade",
        "InsufficientRearmCount",
        "ProtocolOSIncompatibility",
        "MemoryIntegrityIncompatibility",
        "RestrictedDriveLetterInUse",
    )
)


def serialize_aws_json_1_1(value: WorkspaceImageErrorDetailCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceImageErrorDetailCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WorkspaceImageErrorDetailCode value: {data!r}"
        )
    return cast(WorkspaceImageErrorDetailCode, data)
