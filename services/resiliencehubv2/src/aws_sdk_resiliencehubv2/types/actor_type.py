"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ActorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

ActorType: TypeAlias = Literal[
    "USER",
    "SYSTEM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "SYSTEM",
    )
)


def serialize_json(value: ActorType) -> str:
    return value


def deserialize_json(data: str) -> ActorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActorType value: {data!r}")
    return cast(ActorType, data)
