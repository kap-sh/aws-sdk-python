"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association_id


class DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest(TypedDict):
    local_gateway_route_table_virtual_interface_group_association_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association_id.LocalGatewayRouteTableVirtualInterfaceGroupAssociationId"
    ]
    """<p> The ID of the local gateway route table virtual interface group association. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "local_gateway_route_table_virtual_interface_group_association_id" in value:
        pairs.append(
            (
                f"{prefix}.LocalGatewayRouteTableVirtualInterfaceGroupAssociationId",
                str(
                    value[
                        "local_gateway_route_table_virtual_interface_group_association_id"
                    ]
                ),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest:
    out: DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest = {}  # type: ignore[typeddict-item]
    child_local_gateway_route_table_virtual_interface_group_association_id = el.find(
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociationId"
    )
    if (
        child_local_gateway_route_table_virtual_interface_group_association_id
        is not None
    ):
        out["local_gateway_route_table_virtual_interface_group_association_id"] = str(
            child_local_gateway_route_table_virtual_interface_group_association_id.text
            or ""
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
