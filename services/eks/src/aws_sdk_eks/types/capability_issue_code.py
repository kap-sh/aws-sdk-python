"""Generated from Smithy shape ``com.amazonaws.eks#CapabilityIssueCode``."""

from typing import Literal, TypeAlias, cast

CapabilityIssueCode: TypeAlias = Literal[
    "AccessDenied",
    "ClusterUnreachable",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityIssueCode) -> str:
    return value


def deserialize_json(data: str) -> CapabilityIssueCode:
    return cast(CapabilityIssueCode, data)
