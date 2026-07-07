"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeGroupMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.endpoint
    import aws_sdk_elasticache.types.string


class NodeGroupMember(TypedDict, closed=True):
    cache_cluster_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The ID of the cluster to which the node belongs.</p>"""
    cache_node_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).</p>"""
    read_endpoint: NotRequired["aws_sdk_elasticache.types.endpoint.Endpoint"]
    """<p>The information required for client programs to connect to a node for read operations. The read endpoint is only applicable on Valkey or Redis OSS (cluster mode disabled) clusters.</p>"""
    preferred_availability_zone: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the Availability Zone in which the node is located.</p>"""
    preferred_outpost_arn: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The outpost ARN of the node group member.</p>"""
    current_role: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The role that is currently assigned to the node - <code>primary</code> or <code>replica</code>. This member is only applicable for Valkey or Redis OSS (cluster mode disabled) replication groups.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeGroupMember, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_cluster_id" in value:
        pairs.append((f"{prefix}.CacheClusterId", str(value["cache_cluster_id"])))
    if "cache_node_id" in value:
        pairs.append((f"{prefix}.CacheNodeId", str(value["cache_node_id"])))
    if "read_endpoint" in value:
        import aws_sdk_elasticache.types.endpoint

        aws_sdk_elasticache.types.endpoint.serialize_query(
            value["read_endpoint"], pairs, f"{prefix}.ReadEndpoint"
        )
    if "preferred_availability_zone" in value:
        pairs.append(
            (
                f"{prefix}.PreferredAvailabilityZone",
                str(value["preferred_availability_zone"]),
            )
        )
    if "preferred_outpost_arn" in value:
        pairs.append(
            (f"{prefix}.PreferredOutpostArn", str(value["preferred_outpost_arn"]))
        )
    if "current_role" in value:
        pairs.append((f"{prefix}.CurrentRole", str(value["current_role"])))


def deserialize_query(el: Element) -> NodeGroupMember:
    out: NodeGroupMember = {}  # type: ignore[typeddict-item]
    child_cache_cluster_id = el.find("CacheClusterId")
    if child_cache_cluster_id is not None:
        out["cache_cluster_id"] = str(child_cache_cluster_id.text or "")
    child_cache_node_id = el.find("CacheNodeId")
    if child_cache_node_id is not None:
        out["cache_node_id"] = str(child_cache_node_id.text or "")
    child_read_endpoint = el.find("ReadEndpoint")
    if child_read_endpoint is not None:
        import aws_sdk_elasticache.types.endpoint

        out["read_endpoint"] = aws_sdk_elasticache.types.endpoint.deserialize_query(
            child_read_endpoint
        )
    child_preferred_availability_zone = el.find("PreferredAvailabilityZone")
    if child_preferred_availability_zone is not None:
        out["preferred_availability_zone"] = str(
            child_preferred_availability_zone.text or ""
        )
    child_preferred_outpost_arn = el.find("PreferredOutpostArn")
    if child_preferred_outpost_arn is not None:
        out["preferred_outpost_arn"] = str(child_preferred_outpost_arn.text or "")
    child_current_role = el.find("CurrentRole")
    if child_current_role is not None:
        out["current_role"] = str(child_current_role.text or "")
    return out
