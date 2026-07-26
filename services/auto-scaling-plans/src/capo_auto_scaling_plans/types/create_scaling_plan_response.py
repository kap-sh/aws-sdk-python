"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#CreateScalingPlanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_auto_scaling_plans.errors import DeserializationError

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.scaling_plan_version


class CreateScalingPlanResponse(TypedDict, closed=True):
    scaling_plan_version: (
        "capo_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion"
    )
    """<p>The version number of the scaling plan. This value is always <code>1</code>. Currently, you cannot have multiple scaling plan versions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateScalingPlanResponse) -> dict:
    out: dict = {}
    out["ScalingPlanVersion"] = value["scaling_plan_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateScalingPlanResponse:
    out: CreateScalingPlanResponse = {}  # type: ignore[typeddict-item]
    if "ScalingPlanVersion" in data:
        out["scaling_plan_version"] = data["ScalingPlanVersion"]
    else:
        raise DeserializationError(
            "CreateScalingPlanResponse.scaling_plan_version required"
        )
    return out
