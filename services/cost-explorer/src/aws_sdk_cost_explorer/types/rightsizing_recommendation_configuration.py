"""Generated from Smithy shape ``com.amazonaws.costexplorer#RightsizingRecommendationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_boolean
    import aws_sdk_cost_explorer.types.recommendation_target


class RightsizingRecommendationConfiguration(TypedDict, closed=True):
    recommendation_target: (
        "aws_sdk_cost_explorer.types.recommendation_target.RecommendationTarget"
    )
    """<p>The option to see recommendations within the same instance family or recommendations for instances across other families. The default value is <code>SAME_INSTANCE_FAMILY</code>. </p>"""
    benefits_considered: "aws_sdk_cost_explorer.types.generic_boolean.GenericBoolean"
    """<p>The option to consider RI or Savings Plans discount benefits in your savings calculation. The default value is <code>TRUE</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RightsizingRecommendationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_cost_explorer.types.recommendation_target

    out["RecommendationTarget"] = (
        aws_sdk_cost_explorer.types.recommendation_target.serialize_aws_json_1_1(
            value["recommendation_target"]
        )
    )
    out["BenefitsConsidered"] = value.get("benefits_considered", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> RightsizingRecommendationConfiguration:
    out: RightsizingRecommendationConfiguration = {}  # type: ignore[typeddict-item]
    if "RecommendationTarget" in data:
        import aws_sdk_cost_explorer.types.recommendation_target

        out["recommendation_target"] = (
            aws_sdk_cost_explorer.types.recommendation_target.deserialize_aws_json_1_1(
                data["RecommendationTarget"]
            )
        )
    else:
        raise DeserializationError(
            "RightsizingRecommendationConfiguration.recommendation_target required"
        )
    if "BenefitsConsidered" in data:
        out["benefits_considered"] = data["BenefitsConsidered"]
    else:
        out["benefits_considered"] = False
    return out
