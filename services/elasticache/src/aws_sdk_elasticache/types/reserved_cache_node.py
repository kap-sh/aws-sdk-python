"""Generated from Smithy shape ``com.amazonaws.elasticache#ReservedCacheNode``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.double
    import aws_sdk_elasticache.types.integer
    import aws_sdk_elasticache.types.recurring_charge_list
    import aws_sdk_elasticache.types.string
    import aws_sdk_elasticache.types.t_stamp


class ReservedCacheNode(TypedDict):
    reserved_cache_node_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The unique identifier for the reservation.</p>"""
    reserved_cache_nodes_offering_id: NotRequired[
        "aws_sdk_elasticache.types.string.String"
    ]
    """<p>The offering identifier.</p>"""
    cache_node_type: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The cache node type for the reserved cache nodes.</p> <p>The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.</p> <ul> <li> <p>General purpose:</p> <ul> <li> <p>Current generation: </p> <p> <b>M7g node types</b>: <code>cache.m7g.large</code>, <code>cache.m7g.xlarge</code>, <code>cache.m7g.2xlarge</code>, <code>cache.m7g.4xlarge</code>, <code>cache.m7g.8xlarge</code>, <code>cache.m7g.12xlarge</code>, <code>cache.m7g.16xlarge</code> </p> <note> <p>For region availability, see <a href=\"https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion\">Supported Node Types</a> </p> </note> <p> <b>M6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.m6g.large</code>, <code>cache.m6g.xlarge</code>, <code>cache.m6g.2xlarge</code>, <code>cache.m6g.4xlarge</code>, <code>cache.m6g.8xlarge</code>, <code>cache.m6g.12xlarge</code>, <code>cache.m6g.16xlarge</code> </p> <p> <b>M5 node types:</b> <code>cache.m5.large</code>, <code>cache.m5.xlarge</code>, <code>cache.m5.2xlarge</code>, <code>cache.m5.4xlarge</code>, <code>cache.m5.12xlarge</code>, <code>cache.m5.24xlarge</code> </p> <p> <b>M4 node types:</b> <code>cache.m4.large</code>, <code>cache.m4.xlarge</code>, <code>cache.m4.2xlarge</code>, <code>cache.m4.4xlarge</code>, <code>cache.m4.10xlarge</code> </p> <p> <b>T4g node types</b> (available only for Redis OSS engine version 5.0.6 onward and Memcached engine version 1.5.16 onward): <code>cache.t4g.micro</code>, <code>cache.t4g.small</code>, <code>cache.t4g.medium</code> </p> <p> <b>T3 node types:</b> <code>cache.t3.micro</code>, <code>cache.t3.small</code>, <code>cache.t3.medium</code> </p> <p> <b>T2 node types:</b> <code>cache.t2.micro</code>, <code>cache.t2.small</code>, <code>cache.t2.medium</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>T1 node types:</b> <code>cache.t1.micro</code> </p> <p> <b>M1 node types:</b> <code>cache.m1.small</code>, <code>cache.m1.medium</code>, <code>cache.m1.large</code>, <code>cache.m1.xlarge</code> </p> <p> <b>M3 node types:</b> <code>cache.m3.medium</code>, <code>cache.m3.large</code>, <code>cache.m3.xlarge</code>, <code>cache.m3.2xlarge</code> </p> </li> </ul> </li> <li> <p>Compute optimized:</p> <ul> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>C1 node types:</b> <code>cache.c1.xlarge</code> </p> </li> </ul> </li> <li> <p>Memory optimized:</p> <ul> <li> <p>Current generation: </p> <p> <b>R7g node types</b>: <code>cache.r7g.large</code>, <code>cache.r7g.xlarge</code>, <code>cache.r7g.2xlarge</code>, <code>cache.r7g.4xlarge</code>, <code>cache.r7g.8xlarge</code>, <code>cache.r7g.12xlarge</code>, <code>cache.r7g.16xlarge</code> </p> <note> <p>For region availability, see <a href=\"https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion\">Supported Node Types</a> </p> </note> <p> <b>R6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.r6g.large</code>, <code>cache.r6g.xlarge</code>, <code>cache.r6g.2xlarge</code>, <code>cache.r6g.4xlarge</code>, <code>cache.r6g.8xlarge</code>, <code>cache.r6g.12xlarge</code>, <code>cache.r6g.16xlarge</code> </p> <p> <b>R5 node types:</b> <code>cache.r5.large</code>, <code>cache.r5.xlarge</code>, <code>cache.r5.2xlarge</code>, <code>cache.r5.4xlarge</code>, <code>cache.r5.12xlarge</code>, <code>cache.r5.24xlarge</code> </p> <p> <b>R4 node types:</b> <code>cache.r4.large</code>, <code>cache.r4.xlarge</code>, <code>cache.r4.2xlarge</code>, <code>cache.r4.4xlarge</code>, <code>cache.r4.8xlarge</code>, <code>cache.r4.16xlarge</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>M2 node types:</b> <code>cache.m2.xlarge</code>, <code>cache.m2.2xlarge</code>, <code>cache.m2.4xlarge</code> </p> <p> <b>R3 node types:</b> <code>cache.r3.large</code>, <code>cache.r3.xlarge</code>, <code>cache.r3.2xlarge</code>, <code>cache.r3.4xlarge</code>, <code>cache.r3.8xlarge</code> </p> </li> </ul> </li> </ul> <p> <b>Additional node type info</b> </p> <ul> <li> <p>All current generation instance types are created in Amazon VPC by default.</p> </li> <li> <p>Valkey or Redis OSS append-only files (AOF) are not supported for T1 or T2 instances.</p> </li> <li> <p>Valkey or Redis OSS Multi-AZ with automatic failover is not supported on T1 instances.</p> </li> <li> <p>The configuration variables <code>appendonly</code> and <code>appendfsync</code> are not supported on Valkey, or on Redis OSS version 2.8.22 and later.</p> </li> </ul>"""
    start_time: NotRequired["aws_sdk_elasticache.types.t_stamp.TStamp"]
    """<p>The time the reservation started.</p>"""
    duration: NotRequired["aws_sdk_elasticache.types.integer.Integer"]
    """<p>The duration of the reservation in seconds.</p>"""
    fixed_price: NotRequired["aws_sdk_elasticache.types.double.Double"]
    """<p>The fixed price charged for this reserved cache node.</p>"""
    usage_price: NotRequired["aws_sdk_elasticache.types.double.Double"]
    """<p>The hourly price charged for this reserved cache node.</p>"""
    cache_node_count: NotRequired["aws_sdk_elasticache.types.integer.Integer"]
    """<p>The number of cache nodes that have been reserved.</p>"""
    product_description: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The description of the reserved cache node.</p>"""
    offering_type: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The offering type of this reserved cache node.</p>"""
    state: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The state of the reserved cache node.</p>"""
    recurring_charges: NotRequired[
        "aws_sdk_elasticache.types.recurring_charge_list.RecurringChargeList"
    ]
    """<p>The recurring price charged to run this reserved cache node.</p>"""
    reservation_arn: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the reserved cache node.</p> <p>Example: <code>arn:aws:elasticache:us-east-1:123456789012:reserved-instance:ri-2017-03-27-08-33-25-582</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedCacheNode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "reserved_cache_node_id" in value:
        pairs.append(
            (f"{prefix}.ReservedCacheNodeId", str(value["reserved_cache_node_id"]))
        )
    if "reserved_cache_nodes_offering_id" in value:
        pairs.append(
            (
                f"{prefix}.ReservedCacheNodesOfferingId",
                str(value["reserved_cache_nodes_offering_id"]),
            )
        )
    if "cache_node_type" in value:
        pairs.append((f"{prefix}.CacheNodeType", str(value["cache_node_type"])))
    if "start_time" in value:
        import aws_sdk_elasticache.types.t_stamp

        aws_sdk_elasticache.types.t_stamp.serialize_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "duration" in value:
        pairs.append((f"{prefix}.Duration", str(value["duration"])))
    if "fixed_price" in value:
        pairs.append((f"{prefix}.FixedPrice", str(value["fixed_price"])))
    if "usage_price" in value:
        pairs.append((f"{prefix}.UsagePrice", str(value["usage_price"])))
    if "cache_node_count" in value:
        pairs.append((f"{prefix}.CacheNodeCount", str(value["cache_node_count"])))
    if "product_description" in value:
        pairs.append(
            (f"{prefix}.ProductDescription", str(value["product_description"]))
        )
    if "offering_type" in value:
        pairs.append((f"{prefix}.OfferingType", str(value["offering_type"])))
    if "state" in value:
        pairs.append((f"{prefix}.State", str(value["state"])))
    if "recurring_charges" in value:
        import aws_sdk_elasticache.types.recurring_charge_list

        aws_sdk_elasticache.types.recurring_charge_list.serialize_query(
            value["recurring_charges"], pairs, f"{prefix}.RecurringCharges"
        )
    if "reservation_arn" in value:
        pairs.append((f"{prefix}.ReservationARN", str(value["reservation_arn"])))


def deserialize_query(el: Element) -> ReservedCacheNode:
    out: ReservedCacheNode = {}  # type: ignore[typeddict-item]
    child_reserved_cache_node_id = el.find("ReservedCacheNodeId")
    if child_reserved_cache_node_id is not None:
        out["reserved_cache_node_id"] = str(child_reserved_cache_node_id.text or "")
    child_reserved_cache_nodes_offering_id = el.find("ReservedCacheNodesOfferingId")
    if child_reserved_cache_nodes_offering_id is not None:
        out["reserved_cache_nodes_offering_id"] = str(
            child_reserved_cache_nodes_offering_id.text or ""
        )
    child_cache_node_type = el.find("CacheNodeType")
    if child_cache_node_type is not None:
        out["cache_node_type"] = str(child_cache_node_type.text or "")
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import aws_sdk_elasticache.types.t_stamp

        out["start_time"] = aws_sdk_elasticache.types.t_stamp.deserialize_query(
            child_start_time
        )
    child_duration = el.find("Duration")
    if child_duration is not None:
        out["duration"] = int(child_duration.text or "")
    child_fixed_price = el.find("FixedPrice")
    if child_fixed_price is not None:
        out["fixed_price"] = float(child_fixed_price.text or "")
    child_usage_price = el.find("UsagePrice")
    if child_usage_price is not None:
        out["usage_price"] = float(child_usage_price.text or "")
    child_cache_node_count = el.find("CacheNodeCount")
    if child_cache_node_count is not None:
        out["cache_node_count"] = int(child_cache_node_count.text or "")
    child_product_description = el.find("ProductDescription")
    if child_product_description is not None:
        out["product_description"] = str(child_product_description.text or "")
    child_offering_type = el.find("OfferingType")
    if child_offering_type is not None:
        out["offering_type"] = str(child_offering_type.text or "")
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_recurring_charges = el.find("RecurringCharges")
    if child_recurring_charges is not None:
        import aws_sdk_elasticache.types.recurring_charge_list

        out["recurring_charges"] = (
            aws_sdk_elasticache.types.recurring_charge_list.deserialize_query(
                child_recurring_charges
            )
        )
    child_reservation_arn = el.find("ReservationARN")
    if child_reservation_arn is not None:
        out["reservation_arn"] = str(child_reservation_arn.text or "")
    return out
