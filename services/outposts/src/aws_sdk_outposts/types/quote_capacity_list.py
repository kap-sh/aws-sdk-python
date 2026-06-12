"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteCapacityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.quote_capacity

QuoteCapacityList: TypeAlias = list[
    "aws_sdk_outposts.types.quote_capacity.QuoteCapacity"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuoteCapacityList) -> list:
    import aws_sdk_outposts.types.quote_capacity

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.quote_capacity.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuoteCapacityList:
    import aws_sdk_outposts.types.quote_capacity

    out: QuoteCapacityList = []
    for item in data:
        out.append(aws_sdk_outposts.types.quote_capacity.deserialize_json(item))
    return out
