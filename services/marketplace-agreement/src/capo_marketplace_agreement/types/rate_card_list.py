"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RateCardList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.rate_card_item

RateCardList: TypeAlias = list[
    "capo_marketplace_agreement.types.rate_card_item.RateCardItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RateCardList) -> list:
    import capo_marketplace_agreement.types.rate_card_item

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.rate_card_item.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RateCardList:
    import capo_marketplace_agreement.types.rate_card_item

    out: RateCardList = []
    for item in data:
        out.append(
            capo_marketplace_agreement.types.rate_card_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
