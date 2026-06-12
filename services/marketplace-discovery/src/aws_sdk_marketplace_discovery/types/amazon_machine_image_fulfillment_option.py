"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#AmazonMachineImageFulfillmentOption``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_marketplace_discovery.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.amazon_machine_image_operating_system_list
    import aws_sdk_marketplace_discovery.types.amazon_machine_image_recommendation
    import aws_sdk_marketplace_discovery.types.fulfillment_option_type

class AmazonMachineImageFulfillmentOption(TypedDict):
    fulfillment_option_id: "str"
    """<p>The unique identifier of the fulfillment option.</p>"""
    fulfillment_option_name: "str"
    """<p>The display name of the fulfillment option version.</p>"""
    fulfillment_option_version: NotRequired["str"]
    """<p>The version identifier of the fulfillment option.</p>"""
    fulfillment_option_type: "aws_sdk_marketplace_discovery.types.fulfillment_option_type.FulfillmentOptionType"
    """<p>The category of the fulfillment option.</p>"""
    fulfillment_option_display_name: "str"
    """<p>A human-readable name for the fulfillment option type.</p>"""
    operating_systems: "aws_sdk_marketplace_discovery.types.amazon_machine_image_operating_system_list.AmazonMachineImageOperatingSystemList"
    """<p>The operating systems supported by this AMI.</p>"""
    recommendation: NotRequired["aws_sdk_marketplace_discovery.types.amazon_machine_image_recommendation.AmazonMachineImageRecommendation"]
    """<p>Recommended instance types for running this AMI.</p>"""
    release_notes: NotRequired["str"]
    """<p>Release notes describing changes in this version of the fulfillment option.</p>"""
    usage_instructions: NotRequired["str"]
    """<p>Instructions on how to deploy and use this fulfillment option.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AmazonMachineImageFulfillmentOption) -> dict:
    out: dict = {}
    out["fulfillmentOptionId"] = value["fulfillment_option_id"]
    out["fulfillmentOptionName"] = value["fulfillment_option_name"]
    if "fulfillment_option_version" in value:
        out["fulfillmentOptionVersion"] = value["fulfillment_option_version"]
    import aws_sdk_marketplace_discovery.types.fulfillment_option_type
    out["fulfillmentOptionType"] = aws_sdk_marketplace_discovery.types.fulfillment_option_type.serialize_json(value["fulfillment_option_type"])
    out["fulfillmentOptionDisplayName"] = value["fulfillment_option_display_name"]
    import aws_sdk_marketplace_discovery.types.amazon_machine_image_operating_system_list
    out["operatingSystems"] = aws_sdk_marketplace_discovery.types.amazon_machine_image_operating_system_list.serialize_json(value["operating_systems"])
    if "recommendation" in value:
        import aws_sdk_marketplace_discovery.types.amazon_machine_image_recommendation
        out["recommendation"] = aws_sdk_marketplace_discovery.types.amazon_machine_image_recommendation.serialize_json(value["recommendation"])
    if "release_notes" in value:
        out["releaseNotes"] = value["release_notes"]
    if "usage_instructions" in value:
        out["usageInstructions"] = value["usage_instructions"]
    return out


def deserialize_json(data: dict) -> AmazonMachineImageFulfillmentOption:
    out: AmazonMachineImageFulfillmentOption = {}  # type: ignore[typeddict-item]
    if "fulfillmentOptionId" in data:
        out["fulfillment_option_id"] = data["fulfillmentOptionId"]
    else:
        raise DeserializationError("AmazonMachineImageFulfillmentOption.fulfillment_option_id required")
    if "fulfillmentOptionName" in data:
        out["fulfillment_option_name"] = data["fulfillmentOptionName"]
    else:
        raise DeserializationError("AmazonMachineImageFulfillmentOption.fulfillment_option_name required")
    if "fulfillmentOptionVersion" in data:
        out["fulfillment_option_version"] = data["fulfillmentOptionVersion"]
    if "fulfillmentOptionType" in data:
        import aws_sdk_marketplace_discovery.types.fulfillment_option_type
        out["fulfillment_option_type"] = aws_sdk_marketplace_discovery.types.fulfillment_option_type.deserialize_json(data["fulfillmentOptionType"])
    else:
        raise DeserializationError("AmazonMachineImageFulfillmentOption.fulfillment_option_type required")
    if "fulfillmentOptionDisplayName" in data:
        out["fulfillment_option_display_name"] = data["fulfillmentOptionDisplayName"]
    else:
        raise DeserializationError("AmazonMachineImageFulfillmentOption.fulfillment_option_display_name required")
    if "operatingSystems" in data:
        import aws_sdk_marketplace_discovery.types.amazon_machine_image_operating_system_list
        out["operating_systems"] = aws_sdk_marketplace_discovery.types.amazon_machine_image_operating_system_list.deserialize_json(data["operatingSystems"])
    else:
        raise DeserializationError("AmazonMachineImageFulfillmentOption.operating_systems required")
    if "recommendation" in data:
        import aws_sdk_marketplace_discovery.types.amazon_machine_image_recommendation
        out["recommendation"] = aws_sdk_marketplace_discovery.types.amazon_machine_image_recommendation.deserialize_json(data["recommendation"])
    if "releaseNotes" in data:
        out["release_notes"] = data["releaseNotes"]
    if "usageInstructions" in data:
        out["usage_instructions"] = data["usageInstructions"]
    return out