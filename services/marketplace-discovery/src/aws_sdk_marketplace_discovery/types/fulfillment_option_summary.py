"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#FulfillmentOptionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.fulfillment_option_type
    import aws_sdk_marketplace_discovery.types.non_empty_string


class FulfillmentOptionSummary(TypedDict, closed=True):
    fulfillment_option_type: "aws_sdk_marketplace_discovery.types.fulfillment_option_type.FulfillmentOptionType"
    """<p>The machine-readable type of the fulfillment option, such as <code>SAAS</code> or <code>AMAZON_MACHINE_IMAGE</code>.</p>"""
    display_name: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable name of the fulfillment option type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FulfillmentOptionSummary) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_discovery.types.fulfillment_option_type

    out["fulfillmentOptionType"] = (
        aws_sdk_marketplace_discovery.types.fulfillment_option_type.serialize_json(
            value["fulfillment_option_type"]
        )
    )
    out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> FulfillmentOptionSummary:
    out: FulfillmentOptionSummary = {}  # type: ignore[typeddict-item]
    if "fulfillmentOptionType" in data:
        import aws_sdk_marketplace_discovery.types.fulfillment_option_type

        out["fulfillment_option_type"] = (
            aws_sdk_marketplace_discovery.types.fulfillment_option_type.deserialize_json(
                data["fulfillmentOptionType"]
            )
        )
    else:
        raise DeserializationError(
            "FulfillmentOptionSummary.fulfillment_option_type required"
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("FulfillmentOptionSummary.display_name required")
    return out
