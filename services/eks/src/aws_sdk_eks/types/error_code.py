"""Generated from Smithy shape ``com.amazonaws.eks#ErrorCode``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    return cast(ErrorCode, data)
