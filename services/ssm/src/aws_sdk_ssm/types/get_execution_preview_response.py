"""Generated from Smithy shape ``com.amazonaws.ssm#GetExecutionPreviewResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.execution_preview
    import aws_sdk_ssm.types.execution_preview_id
    import aws_sdk_ssm.types.execution_preview_status
    import aws_sdk_ssm.types.string


class GetExecutionPreviewResponse(TypedDict):
    execution_preview_id: NotRequired[
        "aws_sdk_ssm.types.execution_preview_id.ExecutionPreviewId"
    ]
    """<p>The generated ID for the existing execution preview.</p>"""
    ended_at: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>A UTC timestamp indicating when the execution preview operation ended.</p>"""
    status: NotRequired[
        "aws_sdk_ssm.types.execution_preview_status.ExecutionPreviewStatus"
    ]
    """<p>The current status of the execution preview operation.</p>"""
    status_message: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>Supplemental information about the current status of the execution preview.</p>"""
    execution_preview: NotRequired[
        "aws_sdk_ssm.types.execution_preview.ExecutionPreview"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExecutionPreviewResponse) -> dict:
    out: dict = {}
    if "execution_preview_id" in value:
        out["ExecutionPreviewId"] = value["execution_preview_id"]
    if "ended_at" in value:
        import aws_sdk_ssm.types.date_time

        out["EndedAt"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["ended_at"]
        )
    if "status" in value:
        import aws_sdk_ssm.types.execution_preview_status

        out["Status"] = (
            aws_sdk_ssm.types.execution_preview_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "execution_preview" in value:
        import aws_sdk_ssm.types.execution_preview

        out["ExecutionPreview"] = (
            aws_sdk_ssm.types.execution_preview.serialize_aws_json_1_1(
                value["execution_preview"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExecutionPreviewResponse:
    out: GetExecutionPreviewResponse = {}  # type: ignore[typeddict-item]
    if "ExecutionPreviewId" in data:
        out["execution_preview_id"] = data["ExecutionPreviewId"]
    if "EndedAt" in data:
        import aws_sdk_ssm.types.date_time

        out["ended_at"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["EndedAt"]
        )
    if "Status" in data:
        import aws_sdk_ssm.types.execution_preview_status

        out["status"] = (
            aws_sdk_ssm.types.execution_preview_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "ExecutionPreview" in data:
        import aws_sdk_ssm.types.execution_preview

        out["execution_preview"] = (
            aws_sdk_ssm.types.execution_preview.deserialize_aws_json_1_1(
                data["ExecutionPreview"]
            )
        )
    return out
