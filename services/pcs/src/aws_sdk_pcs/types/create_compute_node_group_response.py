"""Generated from Smithy shape ``com.amazonaws.pcs#CreateComputeNodeGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pcs.types.compute_node_group


class CreateComputeNodeGroupResponse(TypedDict, closed=True):
    compute_node_group: NotRequired[
        "aws_sdk_pcs.types.compute_node_group.ComputeNodeGroup"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateComputeNodeGroupResponse) -> dict:
    out: dict = {}
    if "compute_node_group" in value:
        import aws_sdk_pcs.types.compute_node_group

        out["computeNodeGroup"] = (
            aws_sdk_pcs.types.compute_node_group.serialize_aws_json_1_0(
                value["compute_node_group"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateComputeNodeGroupResponse:
    out: CreateComputeNodeGroupResponse = {}  # type: ignore[typeddict-item]
    if "computeNodeGroup" in data:
        import aws_sdk_pcs.types.compute_node_group

        out["compute_node_group"] = (
            aws_sdk_pcs.types.compute_node_group.deserialize_aws_json_1_0(
                data["computeNodeGroup"]
            )
        )
    return out
