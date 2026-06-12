"""Generated from Smithy shape ``com.amazonaws.kafka#GetClusterPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class GetClusterPolicyRequest(TypedDict):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClusterPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetClusterPolicyRequest:
    out: GetClusterPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
