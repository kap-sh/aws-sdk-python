"""Generated from Smithy shape ``com.amazonaws.outposts#PricingOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.pricing_option

PricingOptionList: TypeAlias = list["capo_outposts.types.pricing_option.PricingOption"]


# --- restJson1 ser/de ---
def serialize_json(value: PricingOptionList) -> list:
    import capo_outposts.types.pricing_option

    out: list = []
    for item in value:
        out.append(capo_outposts.types.pricing_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> PricingOptionList:
    import capo_outposts.types.pricing_option

    out: PricingOptionList = []
    for item in data:
        out.append(capo_outposts.types.pricing_option.deserialize_json(item))
    return out
