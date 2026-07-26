"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.quote_specification

QuoteSpecificationList: TypeAlias = list[
    "capo_outposts.types.quote_specification.QuoteSpecification"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuoteSpecificationList) -> list:
    import capo_outposts.types.quote_specification

    out: list = []
    for item in value:
        out.append(capo_outposts.types.quote_specification.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuoteSpecificationList:
    import capo_outposts.types.quote_specification

    out: QuoteSpecificationList = []
    for item in data:
        out.append(capo_outposts.types.quote_specification.deserialize_json(item))
    return out
