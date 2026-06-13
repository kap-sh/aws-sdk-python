"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ConfigurableUpfrontRateCardItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.constraints
    import aws_sdk_marketplace_agreement.types.rate_card_list
    import aws_sdk_marketplace_agreement.types.selector


class ConfigurableUpfrontRateCardItem(TypedDict):
    selector: NotRequired["aws_sdk_marketplace_agreement.types.selector.Selector"]
    """<p>Differentiates between the mutually exclusive rate cards in the same pricing term to be selected by the buyer.</p>"""
    constraints: NotRequired[
        "aws_sdk_marketplace_agreement.types.constraints.Constraints"
    ]
    """<p>Defines limits on how the term can be configured by acceptors.</p>"""
    rate_card: NotRequired[
        "aws_sdk_marketplace_agreement.types.rate_card_list.RateCardList"
    ]
    """<p>Defines the per unit rates for product dimensions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConfigurableUpfrontRateCardItem) -> dict:
    out: dict = {}
    if "selector" in value:
        import aws_sdk_marketplace_agreement.types.selector

        out["selector"] = (
            aws_sdk_marketplace_agreement.types.selector.serialize_aws_json_1_0(
                value["selector"]
            )
        )
    if "constraints" in value:
        import aws_sdk_marketplace_agreement.types.constraints

        out["constraints"] = (
            aws_sdk_marketplace_agreement.types.constraints.serialize_aws_json_1_0(
                value["constraints"]
            )
        )
    if "rate_card" in value:
        import aws_sdk_marketplace_agreement.types.rate_card_list

        out["rateCard"] = (
            aws_sdk_marketplace_agreement.types.rate_card_list.serialize_aws_json_1_0(
                value["rate_card"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConfigurableUpfrontRateCardItem:
    out: ConfigurableUpfrontRateCardItem = {}  # type: ignore[typeddict-item]
    if "selector" in data:
        import aws_sdk_marketplace_agreement.types.selector

        out["selector"] = (
            aws_sdk_marketplace_agreement.types.selector.deserialize_aws_json_1_0(
                data["selector"]
            )
        )
    if "constraints" in data:
        import aws_sdk_marketplace_agreement.types.constraints

        out["constraints"] = (
            aws_sdk_marketplace_agreement.types.constraints.deserialize_aws_json_1_0(
                data["constraints"]
            )
        )
    if "rateCard" in data:
        import aws_sdk_marketplace_agreement.types.rate_card_list

        out["rate_card"] = (
            aws_sdk_marketplace_agreement.types.rate_card_list.deserialize_aws_json_1_0(
                data["rateCard"]
            )
        )
    return out
