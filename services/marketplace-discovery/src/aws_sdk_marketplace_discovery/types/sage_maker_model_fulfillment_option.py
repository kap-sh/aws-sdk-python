"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SageMakerModelFulfillmentOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.fulfillment_option_type
    import aws_sdk_marketplace_discovery.types.sage_maker_model_recommendation


class SageMakerModelFulfillmentOption(TypedDict):
    fulfillment_option_id: "str"
    """<p>The unique identifier of the fulfillment option.</p>"""
    fulfillment_option_type: "aws_sdk_marketplace_discovery.types.fulfillment_option_type.FulfillmentOptionType"
    """<p>The category of the fulfillment option.</p>"""
    fulfillment_option_display_name: "str"
    """<p>A human-readable name for the fulfillment option type.</p>"""
    fulfillment_option_version: NotRequired["str"]
    """<p>The version identifier of the fulfillment option.</p>"""
    release_notes: NotRequired["str"]
    """<p>Release notes describing changes in this version of the fulfillment option.</p>"""
    usage_instructions: NotRequired["str"]
    """<p>Instructions on how to use this SageMaker model.</p>"""
    recommendation: NotRequired[
        "aws_sdk_marketplace_discovery.types.sage_maker_model_recommendation.SageMakerModelRecommendation"
    ]
    """<p>Recommended instance types for inference with this model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerModelFulfillmentOption) -> dict:
    out: dict = {}
    out["fulfillmentOptionId"] = value["fulfillment_option_id"]
    import aws_sdk_marketplace_discovery.types.fulfillment_option_type

    out["fulfillmentOptionType"] = (
        aws_sdk_marketplace_discovery.types.fulfillment_option_type.serialize_json(
            value["fulfillment_option_type"]
        )
    )
    out["fulfillmentOptionDisplayName"] = value["fulfillment_option_display_name"]
    if "fulfillment_option_version" in value:
        out["fulfillmentOptionVersion"] = value["fulfillment_option_version"]
    if "release_notes" in value:
        out["releaseNotes"] = value["release_notes"]
    if "usage_instructions" in value:
        out["usageInstructions"] = value["usage_instructions"]
    if "recommendation" in value:
        import aws_sdk_marketplace_discovery.types.sage_maker_model_recommendation

        out["recommendation"] = (
            aws_sdk_marketplace_discovery.types.sage_maker_model_recommendation.serialize_json(
                value["recommendation"]
            )
        )
    return out


def deserialize_json(data: dict) -> SageMakerModelFulfillmentOption:
    out: SageMakerModelFulfillmentOption = {}  # type: ignore[typeddict-item]
    if "fulfillmentOptionId" in data:
        out["fulfillment_option_id"] = data["fulfillmentOptionId"]
    else:
        raise DeserializationError(
            "SageMakerModelFulfillmentOption.fulfillment_option_id required"
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
            "SageMakerModelFulfillmentOption.fulfillment_option_type required"
        )
    if "fulfillmentOptionDisplayName" in data:
        out["fulfillment_option_display_name"] = data["fulfillmentOptionDisplayName"]
    else:
        raise DeserializationError(
            "SageMakerModelFulfillmentOption.fulfillment_option_display_name required"
        )
    if "fulfillmentOptionVersion" in data:
        out["fulfillment_option_version"] = data["fulfillmentOptionVersion"]
    if "releaseNotes" in data:
        out["release_notes"] = data["releaseNotes"]
    if "usageInstructions" in data:
        out["usage_instructions"] = data["usageInstructions"]
    if "recommendation" in data:
        import aws_sdk_marketplace_discovery.types.sage_maker_model_recommendation

        out["recommendation"] = (
            aws_sdk_marketplace_discovery.types.sage_maker_model_recommendation.deserialize_json(
                data["recommendation"]
            )
        )
    return out
