"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#PipBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ivs_realtime.errors import DeserializationError

PipBehavior: TypeAlias = Literal[
    "STATIC",
    "DYNAMIC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STATIC",
        "DYNAMIC",
    )
)


def serialize_json(value: PipBehavior) -> str:
    return value


def deserialize_json(data: str) -> PipBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PipBehavior value: {data!r}")
    return cast(PipBehavior, data)
