"""Generated from Smithy shape ``com.amazonaws.dsql#GetClusterPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dsql.types.cluster_id


class GetClusterPolicyInput(TypedDict):
    identifier: "aws_sdk_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the cluster to retrieve the policy from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClusterPolicyInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetClusterPolicyInput:
    out: GetClusterPolicyInput = {}  # type: ignore[typeddict-item]
    return out
