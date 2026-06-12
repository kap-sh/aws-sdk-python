"""Generated from Smithy shape ``com.amazonaws.outposts#FiberOpticCableType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

FiberOpticCableType: TypeAlias = Literal[
    "SINGLE_MODE",
    "MULTI_MODE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_MODE",
        "MULTI_MODE",
    )
)


def serialize_json(value: FiberOpticCableType) -> str:
    return value


def deserialize_json(data: str) -> FiberOpticCableType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FiberOpticCableType value: {data!r}")
    return cast(FiberOpticCableType, data)
