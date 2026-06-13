"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#FulfillmentOptionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.fulfillment_option_summary

FulfillmentOptionSummaryList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.fulfillment_option_summary.FulfillmentOptionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FulfillmentOptionSummaryList) -> list:
    import aws_sdk_marketplace_discovery.types.fulfillment_option_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.fulfillment_option_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FulfillmentOptionSummaryList:
    import aws_sdk_marketplace_discovery.types.fulfillment_option_summary

    out: FulfillmentOptionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.fulfillment_option_summary.deserialize_json(
                item
            )
        )
    return out
