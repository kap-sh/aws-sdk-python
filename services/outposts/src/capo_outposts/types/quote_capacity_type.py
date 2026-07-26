"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteCapacityType``."""

from typing import Literal, TypeAlias, cast

QuoteCapacityType: TypeAlias = Literal[
    "EC2",
    "EBS",
    "S3",
]


# --- restJson1 ser/de ---
def serialize_json(value: QuoteCapacityType) -> str:
    return value


def deserialize_json(data: str) -> QuoteCapacityType:
    return cast(QuoteCapacityType, data)
