"""Generated from Smithy shape ``com.amazonaws.iot#DeviceDefenderIndexingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

DeviceDefenderIndexingMode: TypeAlias = Literal[
    "OFF",
    "VIOLATIONS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "VIOLATIONS",
    )
)


def serialize_json(value: DeviceDefenderIndexingMode) -> str:
    return value


def deserialize_json(data: str) -> DeviceDefenderIndexingMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeviceDefenderIndexingMode value: {data!r}"
        )
    return cast(DeviceDefenderIndexingMode, data)
