"""Generated from Smithy shape ``com.amazonaws.eks#CapabilityIssueCode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_eks.errors import DeserializationError

CapabilityIssueCode: TypeAlias = Literal[
    "AccessDenied",
    "ClusterUnreachable",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccessDenied",
        "ClusterUnreachable",
    )
)


def serialize_json(value: CapabilityIssueCode) -> str:
    return value


def deserialize_json(data: str) -> CapabilityIssueCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapabilityIssueCode value: {data!r}")
    return cast(CapabilityIssueCode, data)
