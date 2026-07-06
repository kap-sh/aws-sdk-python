"""Generated from Smithy shape ``com.amazonaws.glue#StopWorkflowRunResponse``."""

from typing_extensions import TypedDict


class StopWorkflowRunResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopWorkflowRunResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopWorkflowRunResponse:
    out: StopWorkflowRunResponse = {}  # type: ignore[typeddict-item]
    return out
