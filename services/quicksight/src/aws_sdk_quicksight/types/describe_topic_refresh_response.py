"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeTopicRefreshResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.topic_refresh_details


class DescribeTopicRefreshResponse(TypedDict):
    refresh_details: NotRequired[
        "aws_sdk_quicksight.types.topic_refresh_details.TopicRefreshDetails"
    ]
    """<p>Details of the refresh, which is performed when the topic is created or updated.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTopicRefreshResponse) -> dict:
    out: dict = {}
    if "refresh_details" in value:
        import aws_sdk_quicksight.types.topic_refresh_details

        out["RefreshDetails"] = (
            aws_sdk_quicksight.types.topic_refresh_details.serialize_json(
                value["refresh_details"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeTopicRefreshResponse:
    out: DescribeTopicRefreshResponse = {}  # type: ignore[typeddict-item]
    if "RefreshDetails" in data:
        import aws_sdk_quicksight.types.topic_refresh_details

        out["refresh_details"] = (
            aws_sdk_quicksight.types.topic_refresh_details.deserialize_json(
                data["RefreshDetails"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
