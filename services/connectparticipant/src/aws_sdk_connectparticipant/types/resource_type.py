"""Generated from Smithy shape ``com.amazonaws.connectparticipant#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "CONTACT",
    "CONTACT_FLOW",
    "INSTANCE",
    "PARTICIPANT",
    "HIERARCHY_LEVEL",
    "HIERARCHY_GROUP",
    "USER",
    "PHONE_NUMBER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    return cast(ResourceType, data)
