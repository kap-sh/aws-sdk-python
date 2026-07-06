"""Generated from Smithy shape ``com.amazonaws.transfer#SendWorkflowStepStateResponse``."""

from typing_extensions import TypedDict


class SendWorkflowStepStateResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendWorkflowStepStateResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> SendWorkflowStepStateResponse:
    out: SendWorkflowStepStateResponse = {}  # type: ignore[typeddict-item]
    return out
