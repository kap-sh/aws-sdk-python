"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeClusterRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class DescribeClusterRequest(TypedDict):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeClusterRequest:
    out: DescribeClusterRequest = {}  # type: ignore[typeddict-item]
    return out
