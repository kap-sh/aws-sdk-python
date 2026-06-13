"""Generated from Smithy shape ``com.amazonaws.pcs#ComputeNodeGroupConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ComputeNodeGroupConfiguration(TypedDict):
    compute_node_group_id: NotRequired["str"]
    """<p>The compute node group ID for the compute node group configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComputeNodeGroupConfiguration) -> dict:
    out: dict = {}
    if "compute_node_group_id" in value:
        out["computeNodeGroupId"] = value["compute_node_group_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ComputeNodeGroupConfiguration:
    out: ComputeNodeGroupConfiguration = {}  # type: ignore[typeddict-item]
    if "computeNodeGroupId" in data:
        out["compute_node_group_id"] = data["computeNodeGroupId"]
    return out
