"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteCapacityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

QuoteCapacityType: TypeAlias = Literal[
    "EC2",
    "EBS",
    "S3",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EC2",
        "EBS",
        "S3",
    )
)


def serialize_json(value: QuoteCapacityType) -> str:
    return value


def deserialize_json(data: str) -> QuoteCapacityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuoteCapacityType value: {data!r}")
    return cast(QuoteCapacityType, data)
