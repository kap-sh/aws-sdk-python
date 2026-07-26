"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeClusterEventResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_event_detail


class DescribeClusterEventResponse(TypedDict, closed=True):
    event_details: NotRequired[
        "capo_sagemaker.types.cluster_event_detail.ClusterEventDetail"
    ]
    """<p>Detailed information about the requested cluster event, including event metadata for various resource types such as <code>Cluster</code>, <code>InstanceGroup</code>, <code>Instance</code>, and their associated attributes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterEventResponse) -> dict:
    out: dict = {}
    if "event_details" in value:
        import capo_sagemaker.types.cluster_event_detail

        out["EventDetails"] = (
            capo_sagemaker.types.cluster_event_detail.serialize_aws_json_1_1(
                value["event_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterEventResponse:
    out: DescribeClusterEventResponse = {}  # type: ignore[typeddict-item]
    if "EventDetails" in data:
        import capo_sagemaker.types.cluster_event_detail

        out["event_details"] = (
            capo_sagemaker.types.cluster_event_detail.deserialize_aws_json_1_1(
                data["EventDetails"]
            )
        )
    return out
