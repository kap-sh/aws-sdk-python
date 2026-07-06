"""Generated from Smithy shape ``com.amazonaws.costexplorer#RightsizingRecommendationMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string
    import aws_sdk_cost_explorer.types.lookback_period_in_days


class RightsizingRecommendationMetadata(TypedDict, closed=True):
    recommendation_id: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The ID for the recommendation.</p>"""
    generation_timestamp: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The timestamp for when Amazon Web Services made the recommendation.</p>"""
    lookback_period_in_days: NotRequired[
        "aws_sdk_cost_explorer.types.lookback_period_in_days.LookbackPeriodInDays"
    ]
    """<p>The number of days of previous usage that Amazon Web Services considers when making the recommendation.</p>"""
    additional_metadata: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>Additional metadata that might be applicable to the recommendation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RightsizingRecommendationMetadata) -> dict:
    out: dict = {}
    if "recommendation_id" in value:
        out["RecommendationId"] = value["recommendation_id"]
    if "generation_timestamp" in value:
        out["GenerationTimestamp"] = value["generation_timestamp"]
    if "lookback_period_in_days" in value:
        import aws_sdk_cost_explorer.types.lookback_period_in_days

        out["LookbackPeriodInDays"] = (
            aws_sdk_cost_explorer.types.lookback_period_in_days.serialize_aws_json_1_1(
                value["lookback_period_in_days"]
            )
        )
    if "additional_metadata" in value:
        out["AdditionalMetadata"] = value["additional_metadata"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RightsizingRecommendationMetadata:
    out: RightsizingRecommendationMetadata = {}  # type: ignore[typeddict-item]
    if "RecommendationId" in data:
        out["recommendation_id"] = data["RecommendationId"]
    if "GenerationTimestamp" in data:
        out["generation_timestamp"] = data["GenerationTimestamp"]
    if "LookbackPeriodInDays" in data:
        import aws_sdk_cost_explorer.types.lookback_period_in_days

        out["lookback_period_in_days"] = (
            aws_sdk_cost_explorer.types.lookback_period_in_days.deserialize_aws_json_1_1(
                data["LookbackPeriodInDays"]
            )
        )
    if "AdditionalMetadata" in data:
        out["additional_metadata"] = data["AdditionalMetadata"]
    return out
