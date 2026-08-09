"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayRouteTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.local_gateway_id
    import capo_ec2.types.local_gateway_route_table_mode
    import capo_ec2.types.tag_specification_list


class CreateLocalGatewayRouteTableRequest(TypedDict, closed=True):
    local_gateway_id: NotRequired["capo_ec2.types.local_gateway_id.LocalGatewayId"]
    """<p> The ID of the local gateway. </p>"""
    mode: NotRequired[
        "capo_ec2.types.local_gateway_route_table_mode.LocalGatewayRouteTableMode"
    ]
    """<p> The mode of the local gateway route table. </p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p> The tags assigned to the local gateway route table. </p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateLocalGatewayRouteTableRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "local_gateway_id" in value:
        pairs.append((f"{key_prefix}LocalGatewayId", str(value["local_gateway_id"])))
    if "mode" in value:
        import capo_ec2.types.local_gateway_route_table_mode

        capo_ec2.types.local_gateway_route_table_mode.serialize_ec2_query(
            value["mode"], pairs, f"{key_prefix}Mode"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateLocalGatewayRouteTableRequest:
    out: CreateLocalGatewayRouteTableRequest = {}  # type: ignore[typeddict-item]
    child_local_gateway_id = el.find("LocalGatewayId")
    if child_local_gateway_id is not None:
        out["local_gateway_id"] = str(child_local_gateway_id.text or "")
    child_mode = el.find("Mode")
    if child_mode is not None:
        import capo_ec2.types.local_gateway_route_table_mode

        out["mode"] = (
            capo_ec2.types.local_gateway_route_table_mode.deserialize_ec2_query(
                child_mode
            )
        )
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
