"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#Role``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

Role: TypeAlias = Literal[
    "CONTROLLER",
    "DEVICE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTROLLER",
        "DEVICE",
    )
)


def serialize_json(value: Role) -> str:
    return value


def deserialize_json(data: str) -> Role:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Role value: {data!r}")
    return cast(Role, data)
