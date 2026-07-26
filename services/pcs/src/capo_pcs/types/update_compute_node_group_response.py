"""Generated from Smithy shape ``com.amazonaws.pcs#UpdateComputeNodeGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.compute_node_group


class UpdateComputeNodeGroupResponse(TypedDict, closed=True):
    compute_node_group: NotRequired[
        "capo_pcs.types.compute_node_group.ComputeNodeGroup"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateComputeNodeGroupResponse) -> dict:
    out: dict = {}
    if "compute_node_group" in value:
        import capo_pcs.types.compute_node_group

        out["computeNodeGroup"] = (
            capo_pcs.types.compute_node_group.serialize_aws_json_1_0(
                value["compute_node_group"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateComputeNodeGroupResponse:
    out: UpdateComputeNodeGroupResponse = {}  # type: ignore[typeddict-item]
    if "computeNodeGroup" in data:
        import capo_pcs.types.compute_node_group

        out["compute_node_group"] = (
            capo_pcs.types.compute_node_group.deserialize_aws_json_1_0(
                data["computeNodeGroup"]
            )
        )
    return out
