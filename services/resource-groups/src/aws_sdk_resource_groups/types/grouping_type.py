"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resource_groups.errors import DeserializationError

GroupingType: TypeAlias = Literal[
    "GROUP",
    "UNGROUP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GROUP",
        "UNGROUP",
    )
)


def serialize_json(value: GroupingType) -> str:
    return value


def deserialize_json(data: str) -> GroupingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupingType value: {data!r}")
    return cast(GroupingType, data)
