"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteCapacityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.quote_capacity

QuoteCapacityList: TypeAlias = list["capo_outposts.types.quote_capacity.QuoteCapacity"]


# --- restJson1 ser/de ---
def serialize_json(value: QuoteCapacityList) -> list:
    import capo_outposts.types.quote_capacity

    out: list = []
    for item in value:
        out.append(capo_outposts.types.quote_capacity.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuoteCapacityList:
    import capo_outposts.types.quote_capacity

    out: QuoteCapacityList = []
    for item in data:
        out.append(capo_outposts.types.quote_capacity.deserialize_json(item))
    return out
