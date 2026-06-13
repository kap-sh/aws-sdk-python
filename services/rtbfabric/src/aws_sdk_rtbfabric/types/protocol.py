"""Generated from Smithy shape ``com.amazonaws.rtbfabric#Protocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rtbfabric.errors import DeserializationError

Protocol: TypeAlias = Literal[
    "HTTP",
    "HTTPS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HTTP",
        "HTTPS",
    )
)


def serialize_json(value: Protocol) -> str:
    return value


def deserialize_json(data: str) -> Protocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Protocol value: {data!r}")
    return cast(Protocol, data)
