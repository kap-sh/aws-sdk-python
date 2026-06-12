"""Generated from Smithy shape ``com.amazonaws.bedrock#RateCard``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.dimensional_price_rate

RateCard: TypeAlias = list[
    "aws_sdk_bedrock.types.dimensional_price_rate.DimensionalPriceRate"
]


# --- restJson1 ser/de ---
def serialize_json(value: RateCard) -> list:
    import aws_sdk_bedrock.types.dimensional_price_rate

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.dimensional_price_rate.serialize_json(item))
    return out


def deserialize_json(data: list) -> RateCard:
    import aws_sdk_bedrock.types.dimensional_price_rate

    out: RateCard = []
    for item in data:
        out.append(aws_sdk_bedrock.types.dimensional_price_rate.deserialize_json(item))
    return out
