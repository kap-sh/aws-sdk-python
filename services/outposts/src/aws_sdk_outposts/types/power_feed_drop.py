"""Generated from Smithy shape ``com.amazonaws.outposts#PowerFeedDrop``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

PowerFeedDrop: TypeAlias = Literal[
    "ABOVE_RACK",
    "BELOW_RACK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ABOVE_RACK",
        "BELOW_RACK",
    )
)


def serialize_json(value: PowerFeedDrop) -> str:
    return value


def deserialize_json(data: str) -> PowerFeedDrop:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PowerFeedDrop value: {data!r}")
    return cast(PowerFeedDrop, data)
