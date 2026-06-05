"""Generated from Smithy shape ``com.amazonaws.ec2#GetRouteServerAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.route_server_id


class GetRouteServerAssociationsRequest(TypedDict):
    route_server_id: NotRequired["aws_sdk_ec2.types.route_server_id.RouteServerId"]
    """<p>The ID of the route server for which to get association information.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetRouteServerAssociationsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route_server_id" in value:
        pairs.append((f"{prefix}.RouteServerId", str(value["route_server_id"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> GetRouteServerAssociationsRequest:
    out: GetRouteServerAssociationsRequest = {}  # type: ignore[typeddict-item]
    child_route_server_id = el.find("RouteServerId")
    if child_route_server_id is not None:
        out["route_server_id"] = str(child_route_server_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
