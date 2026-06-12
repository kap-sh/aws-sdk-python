"""Generated from Smithy shape ``com.amazonaws.guardduty#GroupByType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

GroupByType: TypeAlias = Literal[
    "ACCOUNT",
    "DATE",
    "FINDING_TYPE",
    "RESOURCE",
    "SEVERITY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT",
        "DATE",
        "FINDING_TYPE",
        "RESOURCE",
        "SEVERITY",
    )
)


def serialize_json(value: GroupByType) -> str:
    return value


def deserialize_json(data: str) -> GroupByType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupByType value: {data!r}")
    return cast(GroupByType, data)
