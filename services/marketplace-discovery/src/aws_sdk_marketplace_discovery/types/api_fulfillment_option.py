"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ApiFulfillmentOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.aws_supported_service_list
    import aws_sdk_marketplace_discovery.types.fulfillment_option_type


class ApiFulfillmentOption(TypedDict, closed=True):
    fulfillment_option_id: "str"
    """<p>The unique identifier of the fulfillment option.</p>"""
    fulfillment_option_type: "aws_sdk_marketplace_discovery.types.fulfillment_option_type.FulfillmentOptionType"
    """<p>The category of the fulfillment option.</p>"""
    fulfillment_option_display_name: "str"
    """<p>A human-readable name for the fulfillment option type.</p>"""
    usage_instructions: NotRequired["str"]
    """<p>Instructions on how to integrate with and use this API.</p>"""
    aws_supported_services: "aws_sdk_marketplace_discovery.types.aws_supported_service_list.AwsSupportedServiceList"
    """<p>The AWS services supported by this API integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiFulfillmentOption) -> dict:
    out: dict = {}
    out["fulfillmentOptionId"] = value["fulfillment_option_id"]
    import aws_sdk_marketplace_discovery.types.fulfillment_option_type

    out["fulfillmentOptionType"] = (
        aws_sdk_marketplace_discovery.types.fulfillment_option_type.serialize_json(
            value["fulfillment_option_type"]
        )
    )
    out["fulfillmentOptionDisplayName"] = value["fulfillment_option_display_name"]
    if "usage_instructions" in value:
        out["usageInstructions"] = value["usage_instructions"]
    import aws_sdk_marketplace_discovery.types.aws_supported_service_list

    out["awsSupportedServices"] = (
        aws_sdk_marketplace_discovery.types.aws_supported_service_list.serialize_json(
            value["aws_supported_services"]
        )
    )
    return out


def deserialize_json(data: dict) -> ApiFulfillmentOption:
    out: ApiFulfillmentOption = {}  # type: ignore[typeddict-item]
    if "fulfillmentOptionId" in data:
        out["fulfillment_option_id"] = data["fulfillmentOptionId"]
    else:
        raise DeserializationError(
            "ApiFulfillmentOption.fulfillment_option_id required"
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
            "ApiFulfillmentOption.fulfillment_option_type required"
        )
    if "fulfillmentOptionDisplayName" in data:
        out["fulfillment_option_display_name"] = data["fulfillmentOptionDisplayName"]
    else:
        raise DeserializationError(
            "ApiFulfillmentOption.fulfillment_option_display_name required"
        )
    if "usageInstructions" in data:
        out["usage_instructions"] = data["usageInstructions"]
    if "awsSupportedServices" in data:
        import aws_sdk_marketplace_discovery.types.aws_supported_service_list

        out["aws_supported_services"] = (
            aws_sdk_marketplace_discovery.types.aws_supported_service_list.deserialize_json(
                data["awsSupportedServices"]
            )
        )
    else:
        raise DeserializationError(
            "ApiFulfillmentOption.aws_supported_services required"
        )
    return out
