"""Generated from Smithy shape ``com.amazonaws.eks#AddonIssueCode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_eks.errors import DeserializationError

AddonIssueCode: TypeAlias = Literal[
    "AccessDenied",
    "InternalFailure",
    "ClusterUnreachable",
    "InsufficientNumberOfReplicas",
    "ConfigurationConflict",
    "AdmissionRequestDenied",
    "UnsupportedAddonModification",
    "K8sResourceNotFound",
    "AddonSubscriptionNeeded",
    "AddonPermissionFailure",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccessDenied",
        "InternalFailure",
        "ClusterUnreachable",
        "InsufficientNumberOfReplicas",
        "ConfigurationConflict",
        "AdmissionRequestDenied",
        "UnsupportedAddonModification",
        "K8sResourceNotFound",
        "AddonSubscriptionNeeded",
        "AddonPermissionFailure",
    )
)


def serialize_json(value: AddonIssueCode) -> str:
    return value


def deserialize_json(data: str) -> AddonIssueCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AddonIssueCode value: {data!r}")
    return cast(AddonIssueCode, data)
