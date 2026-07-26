"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeClusterOperationV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class DescribeClusterOperationV2Request(TypedDict, closed=True):
    cluster_operation_arn: "capo_kafka.types.__string.__string"
    """ARN of the cluster operation to describe."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterOperationV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeClusterOperationV2Request:
    out: DescribeClusterOperationV2Request = {}  # type: ignore[typeddict-item]
    return out
