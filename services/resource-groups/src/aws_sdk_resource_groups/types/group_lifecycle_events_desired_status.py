"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupLifecycleEventsDesiredStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resource_groups.errors import DeserializationError

GroupLifecycleEventsDesiredStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_json(value: GroupLifecycleEventsDesiredStatus) -> str:
    return value


def deserialize_json(data: str) -> GroupLifecycleEventsDesiredStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GroupLifecycleEventsDesiredStatus value: {data!r}"
        )
    return cast(GroupLifecycleEventsDesiredStatus, data)
