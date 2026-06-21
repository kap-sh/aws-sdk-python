"""Generated from Smithy shape ``com.amazonaws.eks#FargateProfileIssueCode``."""

from typing import Literal, TypeAlias, cast

FargateProfileIssueCode: TypeAlias = Literal[
    "PodExecutionRoleAlreadyInUse",
    "AccessDenied",
    "ClusterUnreachable",
    "InternalFailure",
]


# --- restJson1 ser/de ---
def serialize_json(value: FargateProfileIssueCode) -> str:
    return value


def deserialize_json(data: str) -> FargateProfileIssueCode:
    return cast(FargateProfileIssueCode, data)
