"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeClusterOperationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class DescribeClusterOperationRequest(TypedDict, closed=True):
    cluster_operation_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the MSK cluster operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterOperationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeClusterOperationRequest:
    out: DescribeClusterOperationRequest = {}  # type: ignore[typeddict-item]
    return out
