"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeGroupUpdateStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.node_group_member_update_status_list
    import aws_sdk_elasticache.types.string


class NodeGroupUpdateStatus(TypedDict, closed=True):
    node_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The ID of the node group</p>"""
    node_group_member_update_status: NotRequired[
        "aws_sdk_elasticache.types.node_group_member_update_status_list.NodeGroupMemberUpdateStatusList"
    ]
    """<p>The status of the service update on the node group member</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeGroupUpdateStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "node_group_id" in value:
        pairs.append((f"{prefix}.NodeGroupId", str(value["node_group_id"])))
    if "node_group_member_update_status" in value:
        import aws_sdk_elasticache.types.node_group_member_update_status_list

        aws_sdk_elasticache.types.node_group_member_update_status_list.serialize_query(
            value["node_group_member_update_status"],
            pairs,
            f"{prefix}.NodeGroupMemberUpdateStatus",
        )


def deserialize_query(el: Element) -> NodeGroupUpdateStatus:
    out: NodeGroupUpdateStatus = {}  # type: ignore[typeddict-item]
    child_node_group_id = el.find("NodeGroupId")
    if child_node_group_id is not None:
        out["node_group_id"] = str(child_node_group_id.text or "")
    child_node_group_member_update_status = el.find("NodeGroupMemberUpdateStatus")
    if child_node_group_member_update_status is not None:
        import aws_sdk_elasticache.types.node_group_member_update_status_list

        out["node_group_member_update_status"] = (
            aws_sdk_elasticache.types.node_group_member_update_status_list.deserialize_query(
                child_node_group_member_update_status
            )
        )
    return out
