"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resource_groups.errors import DeserializationError

GroupConfigurationStatus: TypeAlias = Literal[
    "UPDATING",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPDATING",
        "UPDATE_COMPLETE",
        "UPDATE_FAILED",
    )
)


def serialize_json(value: GroupConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> GroupConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupConfigurationStatus value: {data!r}")
    return cast(GroupConfigurationStatus, data)
