"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#DeleteScalingPlanResponse``."""

from typing_extensions import TypedDict


class DeleteScalingPlanResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteScalingPlanResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteScalingPlanResponse:
    out: DeleteScalingPlanResponse = {}  # type: ignore[typeddict-item]
    return out
