"""Generated from Smithy shape ``com.amazonaws.kafka#PutClusterPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class PutClusterPolicyRequest(TypedDict):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    current_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The policy version.</p>"""
    policy: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutClusterPolicyRequest) -> dict:
    out: dict = {}
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutClusterPolicyRequest:
    out: PutClusterPolicyRequest = {}  # type: ignore[typeddict-item]
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "policy" in data:
        out["policy"] = data["policy"]
    return out
