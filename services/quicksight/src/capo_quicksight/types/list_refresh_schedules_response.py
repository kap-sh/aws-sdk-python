"""Generated from Smithy shape ``com.amazonaws.quicksight#ListRefreshSchedulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.refresh_schedules
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class ListRefreshSchedulesResponse(TypedDict, closed=True):
    refresh_schedules: NotRequired[
        "capo_quicksight.types.refresh_schedules.RefreshSchedules"
    ]
    """<p>The list of refresh schedules for the dataset.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRefreshSchedulesResponse) -> dict:
    out: dict = {}
    if "refresh_schedules" in value:
        import capo_quicksight.types.refresh_schedules

        out["RefreshSchedules"] = (
            capo_quicksight.types.refresh_schedules.serialize_json(
                value["refresh_schedules"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListRefreshSchedulesResponse:
    out: ListRefreshSchedulesResponse = {}  # type: ignore[typeddict-item]
    if "RefreshSchedules" in data:
        import capo_quicksight.types.refresh_schedules

        out["refresh_schedules"] = (
            capo_quicksight.types.refresh_schedules.deserialize_json(
                data["RefreshSchedules"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
