"""Generated from Smithy shape ``com.amazonaws.lambda#StateReasonCode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

StateReasonCode: TypeAlias = Literal[
    "Idle",
    "Creating",
    "Restoring",
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
    "DrainingDurableExecutions",
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
        "Idle",
        "Creating",
        "Restoring",
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
        "DrainingDurableExecutions",
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


def serialize_json(value: StateReasonCode) -> str:
    return value


def deserialize_json(data: str) -> StateReasonCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StateReasonCode value: {data!r}")
    return cast(StateReasonCode, data)
