"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.quote_option

QuoteOptionList: TypeAlias = list["capo_outposts.types.quote_option.QuoteOption"]


# --- restJson1 ser/de ---
def serialize_json(value: QuoteOptionList) -> list:
    import capo_outposts.types.quote_option

    out: list = []
    for item in value:
        out.append(capo_outposts.types.quote_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuoteOptionList:
    import capo_outposts.types.quote_option

    out: QuoteOptionList = []
    for item in data:
        out.append(capo_outposts.types.quote_option.deserialize_json(item))
    return out
