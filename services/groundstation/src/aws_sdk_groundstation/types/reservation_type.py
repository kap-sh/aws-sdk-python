"""Generated from Smithy shape ``com.amazonaws.groundstation#ReservationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

ReservationType: TypeAlias = Literal[
    "MAINTENANCE",
    "CONTACT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MAINTENANCE",
        "CONTACT",
    )
)


def serialize_json(value: ReservationType) -> str:
    return value


def deserialize_json(data: str) -> ReservationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReservationType value: {data!r}")
    return cast(ReservationType, data)
