"""Generated from Smithy shape ``com.amazonaws.quicksight#StartAutomationJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.automate_id
    import aws_sdk_quicksight.types.status_code


class StartAutomationJobResponse(TypedDict):
    arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the automation job.</p>"""
    job_id: "aws_sdk_quicksight.types.automate_id.AutomateId"
    """<p>The ID of the automation job that was started.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAutomationJobResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["JobId"] = value["job_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> StartAutomationJobResponse:
    out: StartAutomationJobResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("StartAutomationJobResponse.arn required")
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("StartAutomationJobResponse.job_id required")
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
