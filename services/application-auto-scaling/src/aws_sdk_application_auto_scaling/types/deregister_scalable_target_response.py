"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#DeregisterScalableTargetResponse``."""

from typing_extensions import TypedDict


class DeregisterScalableTargetResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterScalableTargetResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterScalableTargetResponse:
    out: DeregisterScalableTargetResponse = {}  # type: ignore[typeddict-item]
    return out
