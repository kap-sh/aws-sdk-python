"""Generated from Smithy shape ``com.amazonaws.snowball#DescribeClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.cluster_id


class DescribeClusterRequest(TypedDict, closed=True):
    cluster_id: "aws_sdk_snowball.types.cluster_id.ClusterId"
    """<p>The automatically generated ID for a cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterRequest) -> dict:
    out: dict = {}
    out["ClusterId"] = value["cluster_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterRequest:
    out: DescribeClusterRequest = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    else:
        raise DeserializationError("DescribeClusterRequest.cluster_id required")
    return out
