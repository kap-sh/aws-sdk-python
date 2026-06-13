"""Generated from Smithy shape ``com.amazonaws.quicksight#ListRefreshSchedulesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.refresh_schedules
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class ListRefreshSchedulesResponse(TypedDict):
    refresh_schedules: NotRequired[
        "aws_sdk_quicksight.types.refresh_schedules.RefreshSchedules"
    ]
    """<p>The list of refresh schedules for the dataset.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRefreshSchedulesResponse) -> dict:
    out: dict = {}
    if "refresh_schedules" in value:
        import aws_sdk_quicksight.types.refresh_schedules

        out["RefreshSchedules"] = (
            aws_sdk_quicksight.types.refresh_schedules.serialize_json(
                value["refresh_schedules"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListRefreshSchedulesResponse:
    out: ListRefreshSchedulesResponse = {}  # type: ignore[typeddict-item]
    if "RefreshSchedules" in data:
        import aws_sdk_quicksight.types.refresh_schedules

        out["refresh_schedules"] = (
            aws_sdk_quicksight.types.refresh_schedules.deserialize_json(
                data["RefreshSchedules"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
