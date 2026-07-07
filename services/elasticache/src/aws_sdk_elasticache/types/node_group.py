"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.endpoint
    import aws_sdk_elasticache.types.node_group_member_list
    import aws_sdk_elasticache.types.string


class NodeGroup(TypedDict, closed=True):
    node_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The identifier for the node group (shard). A Valkey or Redis OSS (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Valkey or Redis OSS (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to 0090. Optionally, the user can provide the id for a node group. </p>"""
    status: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The current state of this replication group - <code>creating</code>, <code>available</code>, <code>modifying</code>, <code>deleting</code>.</p>"""
    primary_endpoint: NotRequired["aws_sdk_elasticache.types.endpoint.Endpoint"]
    """<p>The endpoint of the primary node in this node group (shard).</p>"""
    reader_endpoint: NotRequired["aws_sdk_elasticache.types.endpoint.Endpoint"]
    """<p>The endpoint of the replica nodes in this node group (shard). This value is read-only.</p>"""
    slots: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The keyspace for this node group (shard).</p>"""
    node_group_members: NotRequired[
        "aws_sdk_elasticache.types.node_group_member_list.NodeGroupMemberList"
    ]
    """<p>A list containing information about individual nodes within the node group (shard).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "node_group_id" in value:
        pairs.append((f"{prefix}.NodeGroupId", str(value["node_group_id"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "primary_endpoint" in value:
        import aws_sdk_elasticache.types.endpoint

        aws_sdk_elasticache.types.endpoint.serialize_query(
            value["primary_endpoint"], pairs, f"{prefix}.PrimaryEndpoint"
        )
    if "reader_endpoint" in value:
        import aws_sdk_elasticache.types.endpoint

        aws_sdk_elasticache.types.endpoint.serialize_query(
            value["reader_endpoint"], pairs, f"{prefix}.ReaderEndpoint"
        )
    if "slots" in value:
        pairs.append((f"{prefix}.Slots", str(value["slots"])))
    if "node_group_members" in value:
        import aws_sdk_elasticache.types.node_group_member_list

        aws_sdk_elasticache.types.node_group_member_list.serialize_query(
            value["node_group_members"], pairs, f"{prefix}.NodeGroupMembers"
        )


def deserialize_query(el: Element) -> NodeGroup:
    out: NodeGroup = {}  # type: ignore[typeddict-item]
    child_node_group_id = el.find("NodeGroupId")
    if child_node_group_id is not None:
        out["node_group_id"] = str(child_node_group_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_primary_endpoint = el.find("PrimaryEndpoint")
    if child_primary_endpoint is not None:
        import aws_sdk_elasticache.types.endpoint

        out["primary_endpoint"] = aws_sdk_elasticache.types.endpoint.deserialize_query(
            child_primary_endpoint
        )
    child_reader_endpoint = el.find("ReaderEndpoint")
    if child_reader_endpoint is not None:
        import aws_sdk_elasticache.types.endpoint

        out["reader_endpoint"] = aws_sdk_elasticache.types.endpoint.deserialize_query(
            child_reader_endpoint
        )
    child_slots = el.find("Slots")
    if child_slots is not None:
        out["slots"] = str(child_slots.text or "")
    child_node_group_members = el.find("NodeGroupMembers")
    if child_node_group_members is not None:
        import aws_sdk_elasticache.types.node_group_member_list

        out["node_group_members"] = (
            aws_sdk_elasticache.types.node_group_member_list.deserialize_query(
                child_node_group_members
            )
        )
    return out
