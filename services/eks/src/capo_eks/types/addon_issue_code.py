"""Generated from Smithy shape ``com.amazonaws.eks#AddonIssueCode``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: AddonIssueCode) -> str:
    return value


def deserialize_json(data: str) -> AddonIssueCode:
    return cast(AddonIssueCode, data)
