"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#OfferTermsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.offer_term

OfferTermsList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.offer_term.OfferTerm"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferTermsList) -> list:
    import aws_sdk_marketplace_discovery.types.offer_term

    out: list = []
    for item in value:
        out.append(aws_sdk_marketplace_discovery.types.offer_term.serialize_json(item))
    return out


def deserialize_json(data: list) -> OfferTermsList:
    import aws_sdk_marketplace_discovery.types.offer_term

    out: OfferTermsList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.offer_term.deserialize_json(item)
        )
    return out
