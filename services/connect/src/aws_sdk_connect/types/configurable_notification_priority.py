"""Generated from Smithy shape ``com.amazonaws.connect#ConfigurableNotificationPriority``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

"""<p>The priority level that can be set when creating a customer notification. Valid values are HIGH and LOW. URGENT priority is reserved for system-generated notifications.</p>"""
ConfigurableNotificationPriority: TypeAlias = Literal[
    "HIGH",
    "LOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HIGH",
        "LOW",
    )
)


def serialize_json(value: ConfigurableNotificationPriority) -> str:
    return value


def deserialize_json(data: str) -> ConfigurableNotificationPriority:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConfigurableNotificationPriority value: {data!r}"
        )
    return cast(ConfigurableNotificationPriority, data)
