"""Generated from Smithy shape ``com.amazonaws.eks#FargateProfileIssueCode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_eks.errors import DeserializationError

FargateProfileIssueCode: TypeAlias = Literal[
    "PodExecutionRoleAlreadyInUse",
    "AccessDenied",
    "ClusterUnreachable",
    "InternalFailure",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PodExecutionRoleAlreadyInUse",
        "AccessDenied",
        "ClusterUnreachable",
        "InternalFailure",
    )
)


def serialize_json(value: FargateProfileIssueCode) -> str:
    return value


def deserialize_json(data: str) -> FargateProfileIssueCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FargateProfileIssueCode value: {data!r}")
    return cast(FargateProfileIssueCode, data)
