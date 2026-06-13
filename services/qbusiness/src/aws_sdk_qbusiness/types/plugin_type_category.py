"""Generated from Smithy shape ``com.amazonaws.qbusiness#PluginTypeCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

PluginTypeCategory: TypeAlias = Literal[
    "Customer relationship management (CRM)",
    "Project management",
    "Communication",
    "Productivity",
    "Ticketing and incident management",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Customer relationship management (CRM)",
        "Project management",
        "Communication",
        "Productivity",
        "Ticketing and incident management",
    )
)


def serialize_json(value: PluginTypeCategory) -> str:
    return value


def deserialize_json(data: str) -> PluginTypeCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PluginTypeCategory value: {data!r}")
    return cast(PluginTypeCategory, data)
