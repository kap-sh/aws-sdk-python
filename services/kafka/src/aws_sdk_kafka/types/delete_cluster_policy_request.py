"""Generated from Smithy shape ``com.amazonaws.kafka#DeleteClusterPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class DeleteClusterPolicyRequest(TypedDict):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClusterPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteClusterPolicyRequest:
    out: DeleteClusterPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
