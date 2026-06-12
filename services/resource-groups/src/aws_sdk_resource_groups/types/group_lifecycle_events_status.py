"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupLifecycleEventsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resource_groups.errors import DeserializationError

GroupLifecycleEventsStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "IN_PROGRESS",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
        "IN_PROGRESS",
        "ERROR",
    )
)


def serialize_json(value: GroupLifecycleEventsStatus) -> str:
    return value


def deserialize_json(data: str) -> GroupLifecycleEventsStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GroupLifecycleEventsStatus value: {data!r}"
        )
    return cast(GroupLifecycleEventsStatus, data)
