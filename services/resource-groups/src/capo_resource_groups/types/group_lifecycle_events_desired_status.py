"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupLifecycleEventsDesiredStatus``."""

from typing import Literal, TypeAlias, cast

GroupLifecycleEventsDesiredStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupLifecycleEventsDesiredStatus) -> str:
    return value


def deserialize_json(data: str) -> GroupLifecycleEventsDesiredStatus:
    return cast(GroupLifecycleEventsDesiredStatus, data)
