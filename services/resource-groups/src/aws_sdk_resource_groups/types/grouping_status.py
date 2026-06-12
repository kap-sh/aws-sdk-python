"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resource_groups.errors import DeserializationError

GroupingStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAILED",
    "IN_PROGRESS",
    "SKIPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "FAILED",
        "IN_PROGRESS",
        "SKIPPED",
    )
)


def serialize_json(value: GroupingStatus) -> str:
    return value


def deserialize_json(data: str) -> GroupingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupingStatus value: {data!r}")
    return cast(GroupingStatus, data)
