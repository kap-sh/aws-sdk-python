"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeQuickSightQSearchConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.q_search_status
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeQuickSightQSearchConfigurationResponse(TypedDict, closed=True):
    q_search_status: NotRequired["capo_quicksight.types.q_search_status.QSearchStatus"]
    """<p>The status of Quick Sight Q Search configuration.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeQuickSightQSearchConfigurationResponse) -> dict:
    out: dict = {}
    if "q_search_status" in value:
        import capo_quicksight.types.q_search_status

        out["QSearchStatus"] = capo_quicksight.types.q_search_status.serialize_json(
            value["q_search_status"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeQuickSightQSearchConfigurationResponse:
    out: DescribeQuickSightQSearchConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "QSearchStatus" in data:
        import capo_quicksight.types.q_search_status

        out["q_search_status"] = capo_quicksight.types.q_search_status.deserialize_json(
            data["QSearchStatus"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
