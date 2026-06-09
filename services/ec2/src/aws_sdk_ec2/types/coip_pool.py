"""Generated from Smithy shape ``com.amazonaws.ec2#CoipPool``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv4_pool_coip_id
    import aws_sdk_ec2.types.local_gateway_routetable_id
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.value_string_list


class CoipPool(TypedDict):
    pool_id: NotRequired["aws_sdk_ec2.types.ipv4_pool_coip_id.Ipv4PoolCoipId"]
    """<p>The ID of the address pool.</p>"""
    pool_cidrs: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The address ranges of the address pool.</p>"""
    local_gateway_route_table_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_routetable_id.LocalGatewayRoutetableId"
    ]
    """<p>The ID of the local gateway route table.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
    pool_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the address pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CoipPool, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "pool_id" in value:
        pairs.append((f"{prefix}.PoolId", str(value["pool_id"])))
    if "pool_cidrs" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["pool_cidrs"], pairs, f"{prefix}.PoolCidrSet"
        )
    if "local_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{prefix}.LocalGatewayRouteTableId",
                str(value["local_gateway_route_table_id"]),
            )
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "pool_arn" in value:
        pairs.append((f"{prefix}.PoolArn", str(value["pool_arn"])))


def deserialize_ec2_query(el: Element) -> CoipPool:
    out: CoipPool = {}  # type: ignore[typeddict-item]
    child_pool_id = el.find("PoolId")
    if child_pool_id is not None:
        out["pool_id"] = str(child_pool_id.text or "")
    if el.find("PoolCidrSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["pool_cidrs"] = aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
            el, "PoolCidrSet"
        )
    child_local_gateway_route_table_id = el.find("LocalGatewayRouteTableId")
    if child_local_gateway_route_table_id is not None:
        out["local_gateway_route_table_id"] = str(
            child_local_gateway_route_table_id.text or ""
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_pool_arn = el.find("PoolArn")
    if child_pool_arn is not None:
        out["pool_arn"] = str(child_pool_arn.text or "")
    return out
