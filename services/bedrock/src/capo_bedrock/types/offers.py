"""Generated from Smithy shape ``com.amazonaws.bedrock#Offers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.offer

Offers: TypeAlias = list["capo_bedrock.types.offer.Offer"]


# --- restJson1 ser/de ---
def serialize_json(value: Offers) -> list:
    import capo_bedrock.types.offer

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.offer.serialize_json(item))
    return out


def deserialize_json(data: list) -> Offers:
    import capo_bedrock.types.offer

    out: Offers = []
    for item in data:
        out.append(capo_bedrock.types.offer.deserialize_json(item))
    return out
