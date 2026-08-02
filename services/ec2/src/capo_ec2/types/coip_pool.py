"""Generated from Smithy shape ``com.amazonaws.ec2#CoipPool``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipv4_pool_coip_id
    import capo_ec2.types.local_gateway_routetable_id
    import capo_ec2.types.resource_arn
    import capo_ec2.types.tag_list
    import capo_ec2.types.value_string_list


class CoipPool(TypedDict, closed=True):
    pool_id: NotRequired["capo_ec2.types.ipv4_pool_coip_id.Ipv4PoolCoipId"]
    """<p>The ID of the address pool.</p>"""
    pool_cidrs: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The address ranges of the address pool.</p>"""
    local_gateway_route_table_id: NotRequired[
        "capo_ec2.types.local_gateway_routetable_id.LocalGatewayRoutetableId"
    ]
    """<p>The ID of the local gateway route table.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
    pool_arn: NotRequired["capo_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the address pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CoipPool, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "pool_id" in value:
        pairs.append((f"{key_prefix}PoolId", str(value["pool_id"])))
    if "pool_cidrs" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["pool_cidrs"], pairs, f"{key_prefix}PoolCidrSet"
        )
    if "local_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{key_prefix}LocalGatewayRouteTableId",
                str(value["local_gateway_route_table_id"]),
            )
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "pool_arn" in value:
        pairs.append((f"{key_prefix}PoolArn", str(value["pool_arn"])))


def deserialize_ec2_query(el: Element) -> CoipPool:
    out: CoipPool = {}  # type: ignore[typeddict-item]
    child_pool_id = el.find("PoolId")
    if child_pool_id is not None:
        out["pool_id"] = str(child_pool_id.text or "")
    if el.find("PoolCidrSet") is not None:
        import capo_ec2.types.value_string_list

        out["pool_cidrs"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            el, "PoolCidrSet"
        )
    child_local_gateway_route_table_id = el.find("LocalGatewayRouteTableId")
    if child_local_gateway_route_table_id is not None:
        out["local_gateway_route_table_id"] = str(
            child_local_gateway_route_table_id.text or ""
        )
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_pool_arn = el.find("PoolArn")
    if child_pool_arn is not None:
        out["pool_arn"] = str(child_pool_arn.text or "")
    return out
