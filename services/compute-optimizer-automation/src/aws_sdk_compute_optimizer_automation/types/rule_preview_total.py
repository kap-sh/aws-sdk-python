"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RulePreviewTotal``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings


class RulePreviewTotal(TypedDict):
    recommended_action_count: "int"
    """<p>The total number of recommended actions matching the rule preview configuration.</p>"""
    estimated_monthly_savings: "aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings.EstimatedMonthlySavings"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RulePreviewTotal) -> dict:
    out: dict = {}
    out["recommendedActionCount"] = value["recommended_action_count"]
    import aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings

    out["estimatedMonthlySavings"] = (
        aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings.serialize_aws_json_1_0(
            value["estimated_monthly_savings"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RulePreviewTotal:
    out: RulePreviewTotal = {}  # type: ignore[typeddict-item]
    if "recommendedActionCount" in data:
        out["recommended_action_count"] = data["recommendedActionCount"]
    else:
        raise DeserializationError("RulePreviewTotal.recommended_action_count required")
    if "estimatedMonthlySavings" in data:
        import aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimated_monthly_savings"] = (
            aws_sdk_compute_optimizer_automation.types.estimated_monthly_savings.deserialize_aws_json_1_0(
                data["estimatedMonthlySavings"]
            )
        )
    else:
        raise DeserializationError(
            "RulePreviewTotal.estimated_monthly_savings required"
        )
    return out
