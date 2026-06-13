"""Generated from Smithy shape ``com.amazonaws.rtbfabric#LinkDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rtbfabric.errors import DeserializationError

LinkDirection: TypeAlias = Literal[
    "RESPONSE",
    "REQUEST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESPONSE",
        "REQUEST",
    )
)


def serialize_json(value: LinkDirection) -> str:
    return value


def deserialize_json(data: str) -> LinkDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LinkDirection value: {data!r}")
    return cast(LinkDirection, data)
