"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteRackUseType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

QuoteRackUseType: TypeAlias = Literal[
    "NETWORKING",
    "COMPUTE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NETWORKING",
        "COMPUTE",
    )
)


def serialize_json(value: QuoteRackUseType) -> str:
    return value


def deserialize_json(data: str) -> QuoteRackUseType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuoteRackUseType value: {data!r}")
    return cast(QuoteRackUseType, data)
