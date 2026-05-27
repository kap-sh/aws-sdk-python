"""Generated from Smithy shape ``com.amazonaws.lambda#LastUpdateStatusReasonCode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

LastUpdateStatusReasonCode: TypeAlias = Literal[
    "EniLimitExceeded",
    "InsufficientRolePermissions",
    "InvalidConfiguration",
    "InternalError",
    "SubnetOutOfIPAddresses",
    "InvalidSubnet",
    "InvalidSecurityGroup",
    "ImageDeleted",
    "ImageAccessDenied",
    "InvalidImage",
    "KMSKeyAccessDenied",
    "KMSKeyNotFound",
    "InvalidStateKMSKey",
    "DisabledKMSKey",
    "EFSIOError",
    "EFSMountConnectivityError",
    "EFSMountFailure",
    "EFSMountTimeout",
    "InvalidRuntime",
    "InvalidZipFileException",
    "FunctionError",
    "VcpuLimitExceeded",
    "CapacityProviderScalingLimitExceeded",
    "InsufficientCapacity",
    "EC2RequestLimitExceeded",
    "FunctionError.InitTimeout",
    "FunctionError.RuntimeInitError",
    "FunctionError.ExtensionInitError",
    "FunctionError.InvalidEntryPoint",
    "FunctionError.InvalidWorkingDirectory",
    "FunctionError.PermissionDenied",
    "FunctionError.TooManyExtensions",
    "FunctionError.InitResourceExhausted",
    "DisallowedByVpcEncryptionControl",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EniLimitExceeded",
        "InsufficientRolePermissions",
        "InvalidConfiguration",
        "InternalError",
        "SubnetOutOfIPAddresses",
        "InvalidSubnet",
        "InvalidSecurityGroup",
        "ImageDeleted",
        "ImageAccessDenied",
        "InvalidImage",
        "KMSKeyAccessDenied",
        "KMSKeyNotFound",
        "InvalidStateKMSKey",
        "DisabledKMSKey",
        "EFSIOError",
        "EFSMountConnectivityError",
        "EFSMountFailure",
        "EFSMountTimeout",
        "InvalidRuntime",
        "InvalidZipFileException",
        "FunctionError",
        "VcpuLimitExceeded",
        "CapacityProviderScalingLimitExceeded",
        "InsufficientCapacity",
        "EC2RequestLimitExceeded",
        "FunctionError.InitTimeout",
        "FunctionError.RuntimeInitError",
        "FunctionError.ExtensionInitError",
        "FunctionError.InvalidEntryPoint",
        "FunctionError.InvalidWorkingDirectory",
        "FunctionError.PermissionDenied",
        "FunctionError.TooManyExtensions",
        "FunctionError.InitResourceExhausted",
        "DisallowedByVpcEncryptionControl",
    )
)


def serialize_json(value: LastUpdateStatusReasonCode) -> str:
    return value


def deserialize_json(data: str) -> LastUpdateStatusReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LastUpdateStatusReasonCode value: {data!r}"
        )
    return cast(LastUpdateStatusReasonCode, data)
