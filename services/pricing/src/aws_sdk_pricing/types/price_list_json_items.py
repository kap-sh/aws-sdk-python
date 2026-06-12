"""Generated from Smithy shape ``com.amazonaws.pricing#PriceListJsonItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pricing.types.synthesized_json_price_list_json_item

PriceListJsonItems: TypeAlias = list[
    "aws_sdk_pricing.types.synthesized_json_price_list_json_item.SynthesizedJsonPriceListJsonItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PriceListJsonItems) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PriceListJsonItems:
    return list(data)
