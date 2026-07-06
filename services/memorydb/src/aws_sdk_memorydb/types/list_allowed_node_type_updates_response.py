"""Generated from Smithy shape ``com.amazonaws.memorydb#ListAllowedNodeTypeUpdatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.node_type_list


class ListAllowedNodeTypeUpdatesResponse(TypedDict, closed=True):
    scale_up_node_types: NotRequired[
        "aws_sdk_memorydb.types.node_type_list.NodeTypeList"
    ]
    """<p>A list node types which you can use to scale up your cluster.</p>"""
    scale_down_node_types: NotRequired[
        "aws_sdk_memorydb.types.node_type_list.NodeTypeList"
    ]
    """<p>A list node types which you can use to scale down your cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAllowedNodeTypeUpdatesResponse) -> dict:
    out: dict = {}
    if "scale_up_node_types" in value:
        import aws_sdk_memorydb.types.node_type_list

        out["ScaleUpNodeTypes"] = (
            aws_sdk_memorydb.types.node_type_list.serialize_aws_json_1_1(
                value["scale_up_node_types"]
            )
        )
    if "scale_down_node_types" in value:
        import aws_sdk_memorydb.types.node_type_list

        out["ScaleDownNodeTypes"] = (
            aws_sdk_memorydb.types.node_type_list.serialize_aws_json_1_1(
                value["scale_down_node_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAllowedNodeTypeUpdatesResponse:
    out: ListAllowedNodeTypeUpdatesResponse = {}  # type: ignore[typeddict-item]
    if "ScaleUpNodeTypes" in data:
        import aws_sdk_memorydb.types.node_type_list

        out["scale_up_node_types"] = (
            aws_sdk_memorydb.types.node_type_list.deserialize_aws_json_1_1(
                data["ScaleUpNodeTypes"]
            )
        )
    if "ScaleDownNodeTypes" in data:
        import aws_sdk_memorydb.types.node_type_list

        out["scale_down_node_types"] = (
            aws_sdk_memorydb.types.node_type_list.deserialize_aws_json_1_1(
                data["ScaleDownNodeTypes"]
            )
        )
    return out
