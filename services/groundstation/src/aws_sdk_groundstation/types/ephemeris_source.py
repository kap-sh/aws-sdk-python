"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

EphemerisSource: TypeAlias = Literal[
    "CUSTOMER_PROVIDED",
    "SPACE_TRACK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER_PROVIDED",
        "SPACE_TRACK",
    )
)


def serialize_json(value: EphemerisSource) -> str:
    return value


def deserialize_json(data: str) -> EphemerisSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EphemerisSource value: {data!r}")
    return cast(EphemerisSource, data)
