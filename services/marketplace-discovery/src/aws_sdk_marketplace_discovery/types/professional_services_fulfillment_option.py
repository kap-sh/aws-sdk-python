"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ProfessionalServicesFulfillmentOption``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.fulfillment_option_type


class ProfessionalServicesFulfillmentOption(TypedDict, closed=True):
    fulfillment_option_id: "str"
    """<p>The unique identifier of the fulfillment option.</p>"""
    fulfillment_option_type: "aws_sdk_marketplace_discovery.types.fulfillment_option_type.FulfillmentOptionType"
    """<p>The category of the fulfillment option.</p>"""
    fulfillment_option_display_name: "str"
    """<p>A human-readable name for the fulfillment option type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfessionalServicesFulfillmentOption) -> dict:
    out: dict = {}
    out["fulfillmentOptionId"] = value["fulfillment_option_id"]
    import aws_sdk_marketplace_discovery.types.fulfillment_option_type

    out["fulfillmentOptionType"] = (
        aws_sdk_marketplace_discovery.types.fulfillment_option_type.serialize_json(
            value["fulfillment_option_type"]
        )
    )
    out["fulfillmentOptionDisplayName"] = value["fulfillment_option_display_name"]
    return out


def deserialize_json(data: dict) -> ProfessionalServicesFulfillmentOption:
    out: ProfessionalServicesFulfillmentOption = {}  # type: ignore[typeddict-item]
    if "fulfillmentOptionId" in data:
        out["fulfillment_option_id"] = data["fulfillmentOptionId"]
    else:
        raise DeserializationError(
            "ProfessionalServicesFulfillmentOption.fulfillment_option_id required"
        )
    if "fulfillmentOptionType" in data:
        import aws_sdk_marketplace_discovery.types.fulfillment_option_type

        out["fulfillment_option_type"] = (
            aws_sdk_marketplace_discovery.types.fulfillment_option_type.deserialize_json(
                data["fulfillmentOptionType"]
            )
        )
    else:
        raise DeserializationError(
            "ProfessionalServicesFulfillmentOption.fulfillment_option_type required"
        )
    if "fulfillmentOptionDisplayName" in data:
        out["fulfillment_option_display_name"] = data["fulfillmentOptionDisplayName"]
    else:
        raise DeserializationError(
            "ProfessionalServicesFulfillmentOption.fulfillment_option_display_name required"
        )
    return out
