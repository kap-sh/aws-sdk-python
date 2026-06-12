"""Generated from Smithy shape ``com.amazonaws.storagegateway#ErrorCode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_storage_gateway.errors import DeserializationError
from aws_sdk_storage_gateway._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ErrorCode: TypeAlias = Literal[
    "ActivationKeyExpired",
    "ActivationKeyInvalid",
    "ActivationKeyNotFound",
    "GatewayInternalError",
    "GatewayNotConnected",
    "GatewayNotFound",
    "GatewayProxyNetworkConnectionBusy",
    "AuthenticationFailure",
    "BandwidthThrottleScheduleNotFound",
    "Blocked",
    "CannotExportSnapshot",
    "ChapCredentialNotFound",
    "DiskAlreadyAllocated",
    "DiskDoesNotExist",
    "DiskSizeGreaterThanVolumeMaxSize",
    "DiskSizeLessThanVolumeSize",
    "DiskSizeNotGigAligned",
    "DuplicateCertificateInfo",
    "DuplicateSchedule",
    "EndpointNotFound",
    "IAMNotSupported",
    "InitiatorInvalid",
    "InitiatorNotFound",
    "InternalError",
    "InvalidGateway",
    "InvalidEndpoint",
    "InvalidParameters",
    "InvalidSchedule",
    "LocalStorageLimitExceeded",
    "LunAlreadyAllocated ",
    "LunInvalid",
    "JoinDomainInProgress",
    "MaximumContentLengthExceeded",
    "MaximumTapeCartridgeCountExceeded",
    "MaximumVolumeCountExceeded",
    "NetworkConfigurationChanged",
    "NoDisksAvailable",
    "NotImplemented",
    "NotSupported",
    "OperationAborted",
    "OutdatedGateway",
    "ParametersNotImplemented",
    "RegionInvalid",
    "RequestTimeout",
    "ServiceUnavailable",
    "SnapshotDeleted",
    "SnapshotIdInvalid",
    "SnapshotInProgress",
    "SnapshotNotFound",
    "SnapshotScheduleNotFound",
    "StagingAreaFull",
    "StorageFailure",
    "TapeCartridgeNotFound",
    "TargetAlreadyExists",
    "TargetInvalid",
    "TargetNotFound",
    "UnauthorizedOperation",
    "VolumeAlreadyExists",
    "VolumeIdInvalid",
    "VolumeInUse",
    "VolumeNotFound",
    "VolumeNotReady",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ActivationKeyExpired",
        "ActivationKeyInvalid",
        "ActivationKeyNotFound",
        "GatewayInternalError",
        "GatewayNotConnected",
        "GatewayNotFound",
        "GatewayProxyNetworkConnectionBusy",
        "AuthenticationFailure",
        "BandwidthThrottleScheduleNotFound",
        "Blocked",
        "CannotExportSnapshot",
        "ChapCredentialNotFound",
        "DiskAlreadyAllocated",
        "DiskDoesNotExist",
        "DiskSizeGreaterThanVolumeMaxSize",
        "DiskSizeLessThanVolumeSize",
        "DiskSizeNotGigAligned",
        "DuplicateCertificateInfo",
        "DuplicateSchedule",
        "EndpointNotFound",
        "IAMNotSupported",
        "InitiatorInvalid",
        "InitiatorNotFound",
        "InternalError",
        "InvalidGateway",
        "InvalidEndpoint",
        "InvalidParameters",
        "InvalidSchedule",
        "LocalStorageLimitExceeded",
        "LunAlreadyAllocated ",
        "LunInvalid",
        "JoinDomainInProgress",
        "MaximumContentLengthExceeded",
        "MaximumTapeCartridgeCountExceeded",
        "MaximumVolumeCountExceeded",
        "NetworkConfigurationChanged",
        "NoDisksAvailable",
        "NotImplemented",
        "NotSupported",
        "OperationAborted",
        "OutdatedGateway",
        "ParametersNotImplemented",
        "RegionInvalid",
        "RequestTimeout",
        "ServiceUnavailable",
        "SnapshotDeleted",
        "SnapshotIdInvalid",
        "SnapshotInProgress",
        "SnapshotNotFound",
        "SnapshotScheduleNotFound",
        "StagingAreaFull",
        "StorageFailure",
        "TapeCartridgeNotFound",
        "TargetAlreadyExists",
        "TargetInvalid",
        "TargetNotFound",
        "UnauthorizedOperation",
        "VolumeAlreadyExists",
        "VolumeIdInvalid",
        "VolumeInUse",
        "VolumeNotFound",
        "VolumeNotReady",
    )
)


def serialize_aws_json_1_1(value: ErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorCode value: {data!r}")
    return cast(ErrorCode, data)
