"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ConfigurableUpfrontRateCardList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.configurable_upfront_rate_card_item

ConfigurableUpfrontRateCardList: TypeAlias = list[
    "aws_sdk_marketplace_agreement.types.configurable_upfront_rate_card_item.ConfigurableUpfrontRateCardItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConfigurableUpfrontRateCardList) -> list:
    import aws_sdk_marketplace_agreement.types.configurable_upfront_rate_card_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_agreement.types.configurable_upfront_rate_card_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ConfigurableUpfrontRateCardList:
    import aws_sdk_marketplace_agreement.types.configurable_upfront_rate_card_item

    out: ConfigurableUpfrontRateCardList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_agreement.types.configurable_upfront_rate_card_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
