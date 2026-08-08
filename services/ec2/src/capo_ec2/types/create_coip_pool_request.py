"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCoipPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.local_gateway_routetable_id
    import capo_ec2.types.tag_specification_list


class CreateCoipPoolRequest(TypedDict, closed=True):
    local_gateway_route_table_id: NotRequired[
        "capo_ec2.types.local_gateway_routetable_id.LocalGatewayRoutetableId"
    ]
    """<p> The ID of the local gateway route table. </p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p> The tags to assign to the CoIP address pool. </p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCoipPoolRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "local_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{key_prefix}LocalGatewayRouteTableId",
                str(value["local_gateway_route_table_id"]),
            )
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateCoipPoolRequest:
    out: CreateCoipPoolRequest = {}  # type: ignore[typeddict-item]
    child_local_gateway_route_table_id = el.find("LocalGatewayRouteTableId")
    if child_local_gateway_route_table_id is not None:
        out["local_gateway_route_table_id"] = str(
            child_local_gateway_route_table_id.text or ""
        )
    if el.find("TagSpecification") is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecification"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
