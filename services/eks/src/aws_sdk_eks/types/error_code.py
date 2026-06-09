"""Generated from Smithy shape ``com.amazonaws.eks#ErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

ErrorCode: TypeAlias = Literal[
    "SubnetNotFound",
    "SecurityGroupNotFound",
    "EniLimitReached",
    "IpNotAvailable",
    "AccessDenied",
    "OperationNotPermitted",
    "VpcIdNotFound",
    "Unknown",
    "NodeCreationFailure",
    "PodEvictionFailure",
    "InsufficientFreeAddresses",
    "ClusterUnreachable",
    "InsufficientNumberOfReplicas",
    "ConfigurationConflict",
    "AdmissionRequestDenied",
    "UnsupportedAddonModification",
    "K8sResourceNotFound",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SubnetNotFound",
        "SecurityGroupNotFound",
        "EniLimitReached",
        "IpNotAvailable",
        "AccessDenied",
        "OperationNotPermitted",
        "VpcIdNotFound",
        "Unknown",
        "NodeCreationFailure",
        "PodEvictionFailure",
        "InsufficientFreeAddresses",
        "ClusterUnreachable",
        "InsufficientNumberOfReplicas",
        "ConfigurationConflict",
        "AdmissionRequestDenied",
        "UnsupportedAddonModification",
        "K8sResourceNotFound",
    )
)


def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorCode value: {data!r}")
    return cast(ErrorCode, data)
