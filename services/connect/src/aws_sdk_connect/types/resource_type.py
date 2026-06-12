"""Generated from Smithy shape ``com.amazonaws.connect#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "CONTACT",
        "CONTACT_FLOW",
        "INSTANCE",
        "PARTICIPANT",
        "HIERARCHY_LEVEL",
        "HIERARCHY_GROUP",
        "USER",
        "PHONE_NUMBER",
    )
)


def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
