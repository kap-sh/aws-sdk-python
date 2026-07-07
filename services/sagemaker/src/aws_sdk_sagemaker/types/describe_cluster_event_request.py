"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeClusterEventRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_name_or_arn
    import aws_sdk_sagemaker.types.event_id


class DescribeClusterEventRequest(TypedDict, closed=True):
    event_id: NotRequired["aws_sdk_sagemaker.types.event_id.EventId"]
    """<p>The unique identifier (UUID) of the event to describe. This ID can be obtained from the <code>ListClusterEvents</code> operation.</p>"""
    cluster_name: NotRequired[
        "aws_sdk_sagemaker.types.cluster_name_or_arn.ClusterNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the HyperPod cluster associated with the event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterEventRequest) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["EventId"] = value["event_id"]
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterEventRequest:
    out: DescribeClusterEventRequest = {}  # type: ignore[typeddict-item]
    if "EventId" in data:
        out["event_id"] = data["EventId"]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    return out
