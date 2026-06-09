"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRouteTable``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_id
    import aws_sdk_ec2.types.local_gateway_route_table_mode
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.state_reason
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class LocalGatewayRouteTable(TypedDict):
    local_gateway_route_table_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the local gateway route table.</p>"""
    local_gateway_route_table_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the local gateway route table.</p>"""
    local_gateway_id: NotRequired["aws_sdk_ec2.types.local_gateway_id.LocalGatewayId"]
    """<p>The ID of the local gateway.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the local gateway route table.</p>"""
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The state of the local gateway route table.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the local gateway route table.</p>"""
    mode: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_mode.LocalGatewayRouteTableMode"
    ]
    """<p>The mode of the local gateway route table.</p>"""
    state_reason: NotRequired["aws_sdk_ec2.types.state_reason.StateReason"]
    """<p>Information about the state change.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewayRouteTable, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "local_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{prefix}.LocalGatewayRouteTableId",
                str(value["local_gateway_route_table_id"]),
            )
        )
    if "local_gateway_route_table_arn" in value:
        pairs.append(
            (
                f"{prefix}.LocalGatewayRouteTableArn",
                str(value["local_gateway_route_table_arn"]),
            )
        )
    if "local_gateway_id" in value:
        pairs.append((f"{prefix}.LocalGatewayId", str(value["local_gateway_id"])))
    if "outpost_arn" in value:
        pairs.append((f"{prefix}.OutpostArn", str(value["outpost_arn"])))
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "state" in value:
        pairs.append((f"{prefix}.State", str(value["state"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "mode" in value:
        import aws_sdk_ec2.types.local_gateway_route_table_mode

        aws_sdk_ec2.types.local_gateway_route_table_mode.serialize_ec2_query(
            value["mode"], pairs, f"{prefix}.Mode"
        )
    if "state_reason" in value:
        import aws_sdk_ec2.types.state_reason

        aws_sdk_ec2.types.state_reason.serialize_ec2_query(
            value["state_reason"], pairs, f"{prefix}.StateReason"
        )


def deserialize_ec2_query(el: Element) -> LocalGatewayRouteTable:
    out: LocalGatewayRouteTable = {}  # type: ignore[typeddict-item]
    child_local_gateway_route_table_id = el.find("LocalGatewayRouteTableId")
    if child_local_gateway_route_table_id is not None:
        out["local_gateway_route_table_id"] = str(
            child_local_gateway_route_table_id.text or ""
        )
    child_local_gateway_route_table_arn = el.find("LocalGatewayRouteTableArn")
    if child_local_gateway_route_table_arn is not None:
        out["local_gateway_route_table_arn"] = str(
            child_local_gateway_route_table_arn.text or ""
        )
    child_local_gateway_id = el.find("LocalGatewayId")
    if child_local_gateway_id is not None:
        out["local_gateway_id"] = str(child_local_gateway_id.text or "")
    child_outpost_arn = el.find("OutpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_mode = el.find("Mode")
    if child_mode is not None:
        import aws_sdk_ec2.types.local_gateway_route_table_mode

        out["mode"] = (
            aws_sdk_ec2.types.local_gateway_route_table_mode.deserialize_ec2_query(
                child_mode
            )
        )
    child_state_reason = el.find("StateReason")
    if child_state_reason is not None:
        import aws_sdk_ec2.types.state_reason

        out["state_reason"] = aws_sdk_ec2.types.state_reason.deserialize_ec2_query(
            child_state_reason
        )
    return out
