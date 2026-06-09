"""Generated from Smithy shape ``com.amazonaws.eks#ClusterIssueCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

ClusterIssueCode: TypeAlias = Literal[
    "AccessDenied",
    "ClusterUnreachable",
    "ConfigurationConflict",
    "InternalFailure",
    "ResourceLimitExceeded",
    "ResourceNotFound",
    "IamRoleNotFound",
    "VpcNotFound",
    "InsufficientFreeAddresses",
    "Ec2ServiceNotSubscribed",
    "Ec2SubnetNotFound",
    "Ec2SecurityGroupNotFound",
    "KmsGrantRevoked",
    "KmsKeyNotFound",
    "KmsKeyMarkedForDeletion",
    "KmsKeyDisabled",
    "StsRegionalEndpointDisabled",
    "UnsupportedVersion",
    "Other",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccessDenied",
        "ClusterUnreachable",
        "ConfigurationConflict",
        "InternalFailure",
        "ResourceLimitExceeded",
        "ResourceNotFound",
        "IamRoleNotFound",
        "VpcNotFound",
        "InsufficientFreeAddresses",
        "Ec2ServiceNotSubscribed",
        "Ec2SubnetNotFound",
        "Ec2SecurityGroupNotFound",
        "KmsGrantRevoked",
        "KmsKeyNotFound",
        "KmsKeyMarkedForDeletion",
        "KmsKeyDisabled",
        "StsRegionalEndpointDisabled",
        "UnsupportedVersion",
        "Other",
    )
)


def serialize_json(value: ClusterIssueCode) -> str:
    return value


def deserialize_json(data: str) -> ClusterIssueCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterIssueCode value: {data!r}")
    return cast(ClusterIssueCode, data)
