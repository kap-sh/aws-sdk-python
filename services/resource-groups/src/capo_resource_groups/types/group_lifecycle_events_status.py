"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupLifecycleEventsStatus``."""

from typing import Literal, TypeAlias, cast

GroupLifecycleEventsStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "IN_PROGRESS",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupLifecycleEventsStatus) -> str:
    return value


def deserialize_json(data: str) -> GroupLifecycleEventsStatus:
    return cast(GroupLifecycleEventsStatus, data)
