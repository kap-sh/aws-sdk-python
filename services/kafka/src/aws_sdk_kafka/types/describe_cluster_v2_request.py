"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeClusterV2Request``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class DescribeClusterV2Request(TypedDict):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeClusterV2Request:
    out: DescribeClusterV2Request = {}  # type: ignore[typeddict-item]
    return out
