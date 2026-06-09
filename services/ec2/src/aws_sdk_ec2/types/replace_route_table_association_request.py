"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceRouteTableAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.route_table_association_id
    import aws_sdk_ec2.types.route_table_id


class ReplaceRouteTableAssociationRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    association_id: NotRequired[
        "aws_sdk_ec2.types.route_table_association_id.RouteTableAssociationId"
    ]
    """<p>The association ID.</p>"""
    route_table_id: NotRequired["aws_sdk_ec2.types.route_table_id.RouteTableId"]
    """<p>The ID of the new route table to associate with the subnet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReplaceRouteTableAssociationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "association_id" in value:
        pairs.append((f"{prefix}.AssociationId", str(value["association_id"])))
    if "route_table_id" in value:
        pairs.append((f"{prefix}.RouteTableId", str(value["route_table_id"])))


def deserialize_ec2_query(el: Element) -> ReplaceRouteTableAssociationRequest:
    out: ReplaceRouteTableAssociationRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_route_table_id = el.find("RouteTableId")
    if child_route_table_id is not None:
        out["route_table_id"] = str(child_route_table_id.text or "")
    return out
