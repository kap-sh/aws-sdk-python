"""Generated from Smithy shape ``com.amazonaws.bedrock#RateCard``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.dimensional_price_rate

RateCard: TypeAlias = list[
    "capo_bedrock.types.dimensional_price_rate.DimensionalPriceRate"
]


# --- restJson1 ser/de ---
def serialize_json(value: RateCard) -> list:
    import capo_bedrock.types.dimensional_price_rate

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.dimensional_price_rate.serialize_json(item))
    return out


def deserialize_json(data: list) -> RateCard:
    import capo_bedrock.types.dimensional_price_rate

    out: RateCard = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.dimensional_price_rate.deserialize_json(item))
    return out
