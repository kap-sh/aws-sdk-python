"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteRouteServerPeerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.route_server_peer_id


class DeleteRouteServerPeerRequest(TypedDict, closed=True):
    route_server_peer_id: NotRequired[
        "aws_sdk_ec2.types.route_server_peer_id.RouteServerPeerId"
    ]
    """<p>The ID of the route server peer to delete.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteRouteServerPeerRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route_server_peer_id" in value:
        pairs.append(
            (f"{prefix}.RouteServerPeerId", str(value["route_server_peer_id"]))
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteRouteServerPeerRequest:
    out: DeleteRouteServerPeerRequest = {}  # type: ignore[typeddict-item]
    child_route_server_peer_id = el.find("RouteServerPeerId")
    if child_route_server_peer_id is not None:
        out["route_server_peer_id"] = str(child_route_server_peer_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
