"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DescribeTrailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.trail_list


class DescribeTrailsResponse(TypedDict, closed=True):
    trail_list: NotRequired["capo_cloudtrail.types.trail_list.TrailList"]
    """<p>The list of trail objects. Trail objects with string values are only returned if values for the objects exist in a trail's configuration. For example, <code>SNSTopicName</code> and <code>SNSTopicARN</code> are only returned in results if a trail is configured to send SNS notifications. Similarly, <code>KMSKeyId</code> only appears in results if a trail's log files are encrypted with KMS customer managed keys.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrailsResponse) -> dict:
    out: dict = {}
    if "trail_list" in value:
        import capo_cloudtrail.types.trail_list

        out["trailList"] = capo_cloudtrail.types.trail_list.serialize_aws_json_1_1(
            value["trail_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrailsResponse:
    out: DescribeTrailsResponse = {}  # type: ignore[typeddict-item]
    if "trailList" in data:
        import capo_cloudtrail.types.trail_list

        out["trail_list"] = capo_cloudtrail.types.trail_list.deserialize_aws_json_1_1(
            data["trailList"]
        )
    return out
