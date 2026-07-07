"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteRouteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.route_table_id
    import aws_sdk_ec2.types.string


class DeleteRouteRequest(TypedDict, closed=True):
    destination_prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list for the route.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    route_table_id: NotRequired["aws_sdk_ec2.types.route_table_id.RouteTableId"]
    """<p>The ID of the route table.</p>"""
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR range for the route. The value you specify must match the CIDR for the route exactly.</p>"""
    destination_ipv6_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR range for the route. The value you specify must match the CIDR for the route exactly.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteRouteRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "destination_prefix_list_id" in value:
        pairs.append(
            (
                f"{prefix}.DestinationPrefixListId",
                str(value["destination_prefix_list_id"]),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "route_table_id" in value:
        pairs.append((f"{prefix}.RouteTableId", str(value["route_table_id"])))
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{prefix}.DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "destination_ipv6_cidr_block" in value:
        pairs.append(
            (
                f"{prefix}.DestinationIpv6CidrBlock",
                str(value["destination_ipv6_cidr_block"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DeleteRouteRequest:
    out: DeleteRouteRequest = {}  # type: ignore[typeddict-item]
    child_destination_prefix_list_id = el.find("DestinationPrefixListId")
    if child_destination_prefix_list_id is not None:
        out["destination_prefix_list_id"] = str(
            child_destination_prefix_list_id.text or ""
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_route_table_id = el.find("RouteTableId")
    if child_route_table_id is not None:
        out["route_table_id"] = str(child_route_table_id.text or "")
    child_destination_cidr_block = el.find("DestinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_destination_ipv6_cidr_block = el.find("DestinationIpv6CidrBlock")
    if child_destination_ipv6_cidr_block is not None:
        out["destination_ipv6_cidr_block"] = str(
            child_destination_ipv6_cidr_block.text or ""
        )
    return out
