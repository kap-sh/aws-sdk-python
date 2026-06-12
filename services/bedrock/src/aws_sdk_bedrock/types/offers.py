"""Generated from Smithy shape ``com.amazonaws.bedrock#Offers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.offer

Offers: TypeAlias = list["aws_sdk_bedrock.types.offer.Offer"]


# --- restJson1 ser/de ---
def serialize_json(value: Offers) -> list:
    import aws_sdk_bedrock.types.offer

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.offer.serialize_json(item))
    return out


def deserialize_json(data: list) -> Offers:
    import aws_sdk_bedrock.types.offer

    out: Offers = []
    for item in data:
        out.append(aws_sdk_bedrock.types.offer.deserialize_json(item))
    return out
