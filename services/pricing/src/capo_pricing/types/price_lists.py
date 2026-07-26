"""Generated from Smithy shape ``com.amazonaws.pricing#PriceLists``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pricing.types.price_list

PriceLists: TypeAlias = list["capo_pricing.types.price_list.PriceList"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PriceLists) -> list:
    import capo_pricing.types.price_list

    out: list = []
    for item in value:
        out.append(capo_pricing.types.price_list.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PriceLists:
    import capo_pricing.types.price_list

    out: PriceLists = []
    for item in data:
        out.append(capo_pricing.types.price_list.deserialize_aws_json_1_1(item))
    return out
