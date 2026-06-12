"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#EksAddOnFulfillmentOption``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_marketplace_discovery.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.aws_supported_service_list
    import aws_sdk_marketplace_discovery.types.eks_add_on_operating_system_list
    import aws_sdk_marketplace_discovery.types.fulfillment_option_type

class EksAddOnFulfillmentOption(TypedDict):
    fulfillment_option_id: "str"
    """<p>The unique identifier of the fulfillment option.</p>"""
    fulfillment_option_name: "str"
    """<p>The display name of the fulfillment option version.</p>"""
    fulfillment_option_type: "aws_sdk_marketplace_discovery.types.fulfillment_option_type.FulfillmentOptionType"
    """<p>The category of the fulfillment option.</p>"""
    fulfillment_option_display_name: "str"
    """<p>A human-readable name for the fulfillment option type.</p>"""
    fulfillment_option_version: NotRequired["str"]
    """<p>The version identifier of the fulfillment option.</p>"""
    operating_systems: NotRequired["aws_sdk_marketplace_discovery.types.eks_add_on_operating_system_list.EksAddOnOperatingSystemList"]
    """<p>The operating systems supported by this EKS add-on.</p>"""
    release_notes: NotRequired["str"]
    """<p>Release notes describing changes in this version of the fulfillment option.</p>"""
    usage_instructions: NotRequired["str"]
    """<p>Instructions on how to deploy and use this EKS add-on.</p>"""
    aws_supported_services: NotRequired["aws_sdk_marketplace_discovery.types.aws_supported_service_list.AwsSupportedServiceList"]
    """<p>The AWS services supported by this EKS add-on.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: EksAddOnFulfillmentOption) -> dict:
    out: dict = {}
    out["fulfillmentOptionId"] = value["fulfillment_option_id"]
    out["fulfillmentOptionName"] = value["fulfillment_option_name"]
    import aws_sdk_marketplace_discovery.types.fulfillment_option_type
    out["fulfillmentOptionType"] = aws_sdk_marketplace_discovery.types.fulfillment_option_type.serialize_json(value["fulfillment_option_type"])
    out["fulfillmentOptionDisplayName"] = value["fulfillment_option_display_name"]
    if "fulfillment_option_version" in value:
        out["fulfillmentOptionVersion"] = value["fulfillment_option_version"]
    if "operating_systems" in value:
        import aws_sdk_marketplace_discovery.types.eks_add_on_operating_system_list
        out["operatingSystems"] = aws_sdk_marketplace_discovery.types.eks_add_on_operating_system_list.serialize_json(value["operating_systems"])
    if "release_notes" in value:
        out["releaseNotes"] = value["release_notes"]
    if "usage_instructions" in value:
        out["usageInstructions"] = value["usage_instructions"]
    if "aws_supported_services" in value:
        import aws_sdk_marketplace_discovery.types.aws_supported_service_list
        out["awsSupportedServices"] = aws_sdk_marketplace_discovery.types.aws_supported_service_list.serialize_json(value["aws_supported_services"])
    return out


def deserialize_json(data: dict) -> EksAddOnFulfillmentOption:
    out: EksAddOnFulfillmentOption = {}  # type: ignore[typeddict-item]
    if "fulfillmentOptionId" in data:
        out["fulfillment_option_id"] = data["fulfillmentOptionId"]
    else:
        raise DeserializationError("EksAddOnFulfillmentOption.fulfillment_option_id required")
    if "fulfillmentOptionName" in data:
        out["fulfillment_option_name"] = data["fulfillmentOptionName"]
    else:
        raise DeserializationError("EksAddOnFulfillmentOption.fulfillment_option_name required")
    if "fulfillmentOptionType" in data:
        import aws_sdk_marketplace_discovery.types.fulfillment_option_type
        out["fulfillment_option_type"] = aws_sdk_marketplace_discovery.types.fulfillment_option_type.deserialize_json(data["fulfillmentOptionType"])
    else:
        raise DeserializationError("EksAddOnFulfillmentOption.fulfillment_option_type required")
    if "fulfillmentOptionDisplayName" in data:
        out["fulfillment_option_display_name"] = data["fulfillmentOptionDisplayName"]
    else:
        raise DeserializationError("EksAddOnFulfillmentOption.fulfillment_option_display_name required")
    if "fulfillmentOptionVersion" in data:
        out["fulfillment_option_version"] = data["fulfillmentOptionVersion"]
    if "operatingSystems" in data:
        import aws_sdk_marketplace_discovery.types.eks_add_on_operating_system_list
        out["operating_systems"] = aws_sdk_marketplace_discovery.types.eks_add_on_operating_system_list.deserialize_json(data["operatingSystems"])
    if "releaseNotes" in data:
        out["release_notes"] = data["releaseNotes"]
    if "usageInstructions" in data:
        out["usage_instructions"] = data["usageInstructions"]
    if "awsSupportedServices" in data:
        import aws_sdk_marketplace_discovery.types.aws_supported_service_list
        out["aws_supported_services"] = aws_sdk_marketplace_discovery.types.aws_supported_service_list.deserialize_json(data["awsSupportedServices"])
    return out