"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateQuickSightQSearchConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.q_search_status
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateQuickSightQSearchConfigurationResponse(TypedDict):
    q_search_status: NotRequired[
        "aws_sdk_quicksight.types.q_search_status.QSearchStatus"
    ]
    """<p>The status of the Quick Sight Q Search configuration.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQuickSightQSearchConfigurationResponse) -> dict:
    out: dict = {}
    if "q_search_status" in value:
        import aws_sdk_quicksight.types.q_search_status

        out["QSearchStatus"] = aws_sdk_quicksight.types.q_search_status.serialize_json(
            value["q_search_status"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateQuickSightQSearchConfigurationResponse:
    out: UpdateQuickSightQSearchConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "QSearchStatus" in data:
        import aws_sdk_quicksight.types.q_search_status

        out["q_search_status"] = (
            aws_sdk_quicksight.types.q_search_status.deserialize_json(
                data["QSearchStatus"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
