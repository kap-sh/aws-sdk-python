"""Generated from Smithy shape ``com.amazonaws.guardduty#GroupByType``."""

from typing import Literal, TypeAlias, cast

GroupByType: TypeAlias = Literal[
    "ACCOUNT",
    "DATE",
    "FINDING_TYPE",
    "RESOURCE",
    "SEVERITY",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupByType) -> str:
    return value


def deserialize_json(data: str) -> GroupByType:
    return cast(GroupByType, data)
