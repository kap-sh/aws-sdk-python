"""Generated from Smithy shape ``com.amazonaws.storagegateway#ErrorCode``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: ErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ErrorCode:
    return cast(ErrorCode, data)
