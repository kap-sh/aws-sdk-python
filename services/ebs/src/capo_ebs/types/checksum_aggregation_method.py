"""Generated from Smithy shape ``com.amazonaws.ebs#ChecksumAggregationMethod``."""

from typing import Literal, TypeAlias, cast

ChecksumAggregationMethod: TypeAlias = Literal["LINEAR",]


# --- restJson1 ser/de ---
def serialize_json(value: ChecksumAggregationMethod) -> str:
    return value


def deserialize_json(data: str) -> ChecksumAggregationMethod:
    return cast(ChecksumAggregationMethod, data)
