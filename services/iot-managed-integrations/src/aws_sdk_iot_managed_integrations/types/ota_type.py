"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

OtaType: TypeAlias = Literal[
    "ONE_TIME",
    "CONTINUOUS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONE_TIME",
        "CONTINUOUS",
    )
)


def serialize_json(value: OtaType) -> str:
    return value


def deserialize_json(data: str) -> OtaType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OtaType value: {data!r}")
    return cast(OtaType, data)
