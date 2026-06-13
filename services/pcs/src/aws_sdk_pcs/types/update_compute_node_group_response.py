"""Generated from Smithy shape ``com.amazonaws.pcs#UpdateComputeNodeGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pcs.types.compute_node_group


class UpdateComputeNodeGroupResponse(TypedDict):
    compute_node_group: NotRequired[
        "aws_sdk_pcs.types.compute_node_group.ComputeNodeGroup"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateComputeNodeGroupResponse) -> dict:
    out: dict = {}
    if "compute_node_group" in value:
        import aws_sdk_pcs.types.compute_node_group

        out["computeNodeGroup"] = (
            aws_sdk_pcs.types.compute_node_group.serialize_aws_json_1_0(
                value["compute_node_group"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateComputeNodeGroupResponse:
    out: UpdateComputeNodeGroupResponse = {}  # type: ignore[typeddict-item]
    if "computeNodeGroup" in data:
        import aws_sdk_pcs.types.compute_node_group

        out["compute_node_group"] = (
            aws_sdk_pcs.types.compute_node_group.deserialize_aws_json_1_0(
                data["computeNodeGroup"]
            )
        )
    return out
