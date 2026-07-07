"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateRefreshScheduleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateRefreshScheduleResponse(TypedDict, closed=True):
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    schedule_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The ID of the refresh schedule.</p>"""
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the refresh schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRefreshScheduleResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "schedule_id" in value:
        out["ScheduleId"] = value["schedule_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> UpdateRefreshScheduleResponse:
    out: UpdateRefreshScheduleResponse = {}  # type: ignore[typeddict-item]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "ScheduleId" in data:
        out["schedule_id"] = data["ScheduleId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
