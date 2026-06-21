"""Generated from Smithy shape ``com.amazonaws.eks#ClusterIssueCode``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ClusterIssueCode) -> str:
    return value


def deserialize_json(data: str) -> ClusterIssueCode:
    return cast(ClusterIssueCode, data)
