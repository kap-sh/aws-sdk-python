"""Generated from Smithy shape ``com.amazonaws.kafka#DeleteClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class DeleteClusterRequest(TypedDict, closed=True):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    current_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The current version of the MSK cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClusterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteClusterRequest:
    out: DeleteClusterRequest = {}  # type: ignore[typeddict-item]
    return out
