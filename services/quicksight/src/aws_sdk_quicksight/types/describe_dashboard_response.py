"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDashboardResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dashboard
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeDashboardResponse(TypedDict):
    dashboard: NotRequired["aws_sdk_quicksight.types.dashboard.Dashboard"]
    """<p>Information about the dashboard.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of this request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDashboardResponse) -> dict:
    out: dict = {}
    if "dashboard" in value:
        import aws_sdk_quicksight.types.dashboard

        out["Dashboard"] = aws_sdk_quicksight.types.dashboard.serialize_json(
            value["dashboard"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeDashboardResponse:
    out: DescribeDashboardResponse = {}  # type: ignore[typeddict-item]
    if "Dashboard" in data:
        import aws_sdk_quicksight.types.dashboard

        out["dashboard"] = aws_sdk_quicksight.types.dashboard.deserialize_json(
            data["Dashboard"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
