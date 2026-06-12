"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheNode``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.endpoint
    import aws_sdk_elasticache.types.string
    import aws_sdk_elasticache.types.t_stamp


class CacheNode(TypedDict):
    cache_node_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The combination of cluster ID and node ID uniquely identifies every cache node used in a customer's Amazon account.</p>"""
    cache_node_status: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The current state of this cache node, one of the following values: <code>available</code>, <code>creating</code>, <code>rebooting</code>, or <code>deleting</code>.</p>"""
    cache_node_create_time: NotRequired["aws_sdk_elasticache.types.t_stamp.TStamp"]
    """<p>The date and time when the cache node was created.</p>"""
    endpoint: NotRequired["aws_sdk_elasticache.types.endpoint.Endpoint"]
    """<p>The hostname for connecting to this cache node.</p>"""
    parameter_group_status: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The status of the parameter group applied to this cache node.</p>"""
    source_cache_node_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The ID of the primary node to which this read replica node is synchronized. If this field is empty, this node is not associated with a primary cluster.</p>"""
    customer_availability_zone: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The Availability Zone where this node was created and now resides.</p>"""
    customer_outpost_arn: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The customer outpost ARN of the cache node.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheNode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_node_id" in value:
        pairs.append((f"{prefix}.CacheNodeId", str(value["cache_node_id"])))
    if "cache_node_status" in value:
        pairs.append((f"{prefix}.CacheNodeStatus", str(value["cache_node_status"])))
    if "cache_node_create_time" in value:
        import aws_sdk_elasticache.types.t_stamp

        aws_sdk_elasticache.types.t_stamp.serialize_query(
            value["cache_node_create_time"], pairs, f"{prefix}.CacheNodeCreateTime"
        )
    if "endpoint" in value:
        import aws_sdk_elasticache.types.endpoint

        aws_sdk_elasticache.types.endpoint.serialize_query(
            value["endpoint"], pairs, f"{prefix}.Endpoint"
        )
    if "parameter_group_status" in value:
        pairs.append(
            (f"{prefix}.ParameterGroupStatus", str(value["parameter_group_status"]))
        )
    if "source_cache_node_id" in value:
        pairs.append(
            (f"{prefix}.SourceCacheNodeId", str(value["source_cache_node_id"]))
        )
    if "customer_availability_zone" in value:
        pairs.append(
            (
                f"{prefix}.CustomerAvailabilityZone",
                str(value["customer_availability_zone"]),
            )
        )
    if "customer_outpost_arn" in value:
        pairs.append(
            (f"{prefix}.CustomerOutpostArn", str(value["customer_outpost_arn"]))
        )


def deserialize_query(el: Element) -> CacheNode:
    out: CacheNode = {}  # type: ignore[typeddict-item]
    child_cache_node_id = el.find("CacheNodeId")
    if child_cache_node_id is not None:
        out["cache_node_id"] = str(child_cache_node_id.text or "")
    child_cache_node_status = el.find("CacheNodeStatus")
    if child_cache_node_status is not None:
        out["cache_node_status"] = str(child_cache_node_status.text or "")
    child_cache_node_create_time = el.find("CacheNodeCreateTime")
    if child_cache_node_create_time is not None:
        import aws_sdk_elasticache.types.t_stamp

        out["cache_node_create_time"] = (
            aws_sdk_elasticache.types.t_stamp.deserialize_query(
                child_cache_node_create_time
            )
        )
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        import aws_sdk_elasticache.types.endpoint

        out["endpoint"] = aws_sdk_elasticache.types.endpoint.deserialize_query(
            child_endpoint
        )
    child_parameter_group_status = el.find("ParameterGroupStatus")
    if child_parameter_group_status is not None:
        out["parameter_group_status"] = str(child_parameter_group_status.text or "")
    child_source_cache_node_id = el.find("SourceCacheNodeId")
    if child_source_cache_node_id is not None:
        out["source_cache_node_id"] = str(child_source_cache_node_id.text or "")
    child_customer_availability_zone = el.find("CustomerAvailabilityZone")
    if child_customer_availability_zone is not None:
        out["customer_availability_zone"] = str(
            child_customer_availability_zone.text or ""
        )
    child_customer_outpost_arn = el.find("CustomerOutpostArn")
    if child_customer_outpost_arn is not None:
        out["customer_outpost_arn"] = str(child_customer_outpost_arn.text or "")
    return out
