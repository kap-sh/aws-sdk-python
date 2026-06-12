"""Generated from Smithy shape ``com.amazonaws.kafka#ListClusterOperationsV2Request``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.max_results


class ListClusterOperationsV2Request(TypedDict):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """The arn of the cluster whose operations are being requested."""
    max_results: NotRequired["aws_sdk_kafka.types.max_results.MaxResults"]
    """The maxResults of the query."""
    next_token: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """The nextToken of the query."""


# --- restJson1 ser/de ---
def serialize_json(value: ListClusterOperationsV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListClusterOperationsV2Request:
    out: ListClusterOperationsV2Request = {}  # type: ignore[typeddict-item]
    return out
