"""Generated from Smithy shape ``com.amazonaws.elasticache#TestFailoverMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.allowed_node_group_id
    import capo_elasticache.types.string


class TestFailoverMessage(TypedDict, closed=True):
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the replication group (console: cluster) whose automatic failover is being tested by this operation.</p>"""
    node_group_id: NotRequired[
        "capo_elasticache.types.allowed_node_group_id.AllowedNodeGroupId"
    ]
    """<p>The name of the node group (called shard in the console) in this replication group on which automatic failover is to be tested. You may test automatic failover on up to 15 node groups in any rolling 24-hour period.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TestFailoverMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "replication_group_id" in value:
        pairs.append(
            (f"{key_prefix}ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "node_group_id" in value:
        pairs.append((f"{key_prefix}NodeGroupId", str(value["node_group_id"])))


def deserialize_query(el: Element) -> TestFailoverMessage:
    out: TestFailoverMessage = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_node_group_id = el.find("NodeGroupId")
    if child_node_group_id is not None:
        out["node_group_id"] = str(child_node_group_id.text or "")
    return out
