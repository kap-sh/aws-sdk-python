"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#DeleteScalingPolicyResponse``."""

from typing_extensions import TypedDict


class DeleteScalingPolicyResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteScalingPolicyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteScalingPolicyResponse:
    out: DeleteScalingPolicyResponse = {}  # type: ignore[typeddict-item]
    return out
