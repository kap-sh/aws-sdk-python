"""Generated from Smithy shape ``com.amazonaws.ssm#GetExecutionPreviewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.execution_preview_id


class GetExecutionPreviewRequest(TypedDict, closed=True):
    execution_preview_id: "aws_sdk_ssm.types.execution_preview_id.ExecutionPreviewId"
    """<p>The ID of the existing execution preview.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExecutionPreviewRequest) -> dict:
    out: dict = {}
    out["ExecutionPreviewId"] = value["execution_preview_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExecutionPreviewRequest:
    out: GetExecutionPreviewRequest = {}  # type: ignore[typeddict-item]
    if "ExecutionPreviewId" in data:
        out["execution_preview_id"] = data["ExecutionPreviewId"]
    else:
        raise DeserializationError(
            "GetExecutionPreviewRequest.execution_preview_id required"
        )
    return out
