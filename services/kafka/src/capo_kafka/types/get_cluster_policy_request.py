"""Generated from Smithy shape ``com.amazonaws.kafka#GetClusterPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class GetClusterPolicyRequest(TypedDict, closed=True):
    cluster_arn: "capo_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClusterPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetClusterPolicyRequest:
    out: GetClusterPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
