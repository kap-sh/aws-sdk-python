"""Generated from Smithy shape ``com.amazonaws.kafka#ListClusterOperationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.max_results


class ListClusterOperationsRequest(TypedDict, closed=True):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    max_results: NotRequired["aws_sdk_kafka.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>"""
    next_token: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClusterOperationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListClusterOperationsRequest:
    out: ListClusterOperationsRequest = {}  # type: ignore[typeddict-item]
    return out
