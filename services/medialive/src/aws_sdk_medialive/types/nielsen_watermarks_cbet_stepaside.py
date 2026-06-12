"""Generated from Smithy shape ``com.amazonaws.medialive#NielsenWatermarksCbetStepaside``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Nielsen Watermarks Cbet Stepaside"""
NielsenWatermarksCbetStepaside: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: NielsenWatermarksCbetStepaside) -> str:
    return value


def deserialize_json(data: str) -> NielsenWatermarksCbetStepaside:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NielsenWatermarksCbetStepaside value: {data!r}"
        )
    return cast(NielsenWatermarksCbetStepaside, data)
