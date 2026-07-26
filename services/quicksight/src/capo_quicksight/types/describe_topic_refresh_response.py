"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeTopicRefreshResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.topic_refresh_details


class DescribeTopicRefreshResponse(TypedDict, closed=True):
    refresh_details: NotRequired[
        "capo_quicksight.types.topic_refresh_details.TopicRefreshDetails"
    ]
    """<p>Details of the refresh, which is performed when the topic is created or updated.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTopicRefreshResponse) -> dict:
    out: dict = {}
    if "refresh_details" in value:
        import capo_quicksight.types.topic_refresh_details

        out["RefreshDetails"] = (
            capo_quicksight.types.topic_refresh_details.serialize_json(
                value["refresh_details"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeTopicRefreshResponse:
    out: DescribeTopicRefreshResponse = {}  # type: ignore[typeddict-item]
    if "RefreshDetails" in data:
        import capo_quicksight.types.topic_refresh_details

        out["refresh_details"] = (
            capo_quicksight.types.topic_refresh_details.deserialize_json(
                data["RefreshDetails"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
