"""Generated from Smithy shape ``com.amazonaws.memorydb#ListAllowedMultiRegionClusterUpdatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.node_type_list


class ListAllowedMultiRegionClusterUpdatesResponse(TypedDict, closed=True):
    scale_up_node_types: NotRequired["capo_memorydb.types.node_type_list.NodeTypeList"]
    """<p>The node types that the cluster can be scaled up to.</p>"""
    scale_down_node_types: NotRequired[
        "capo_memorydb.types.node_type_list.NodeTypeList"
    ]
    """<p>The node types that the cluster can be scaled down to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAllowedMultiRegionClusterUpdatesResponse) -> dict:
    out: dict = {}
    if "scale_up_node_types" in value:
        import capo_memorydb.types.node_type_list

        out["ScaleUpNodeTypes"] = (
            capo_memorydb.types.node_type_list.serialize_aws_json_1_1(
                value["scale_up_node_types"]
            )
        )
    if "scale_down_node_types" in value:
        import capo_memorydb.types.node_type_list

        out["ScaleDownNodeTypes"] = (
            capo_memorydb.types.node_type_list.serialize_aws_json_1_1(
                value["scale_down_node_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListAllowedMultiRegionClusterUpdatesResponse:
    out: ListAllowedMultiRegionClusterUpdatesResponse = {}  # type: ignore[typeddict-item]
    if "ScaleUpNodeTypes" in data:
        import capo_memorydb.types.node_type_list

        out["scale_up_node_types"] = (
            capo_memorydb.types.node_type_list.deserialize_aws_json_1_1(
                data["ScaleUpNodeTypes"]
            )
        )
    if "ScaleDownNodeTypes" in data:
        import capo_memorydb.types.node_type_list

        out["scale_down_node_types"] = (
            capo_memorydb.types.node_type_list.deserialize_aws_json_1_1(
                data["ScaleDownNodeTypes"]
            )
        )
    return out
