"""Generated from Smithy shape ``com.amazonaws.appconfig#GrowthType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appconfig.errors import DeserializationError

GrowthType: TypeAlias = Literal[
    "LINEAR",
    "EXPONENTIAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LINEAR",
        "EXPONENTIAL",
    )
)


def serialize_json(value: GrowthType) -> str:
    return value


def deserialize_json(data: str) -> GrowthType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GrowthType value: {data!r}")
    return cast(GrowthType, data)
