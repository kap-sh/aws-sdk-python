"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

GroupConfigurationStatus: TypeAlias = Literal[
    "UPDATING",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> GroupConfigurationStatus:
    return cast(GroupConfigurationStatus, data)
