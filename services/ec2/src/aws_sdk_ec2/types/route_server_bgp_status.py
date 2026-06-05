"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerBgpStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_bgp_state


class RouteServerBgpStatus(TypedDict):
    status: NotRequired["aws_sdk_ec2.types.route_server_bgp_state.RouteServerBgpState"]
    """<p>The operational status of the BGP session. The status enables you to monitor session liveness if you lack monitoring on your router/appliance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerBgpStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "status" in value:
        import aws_sdk_ec2.types.route_server_bgp_state

        aws_sdk_ec2.types.route_server_bgp_state.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_ec2_query(el: Element) -> RouteServerBgpStatus:
    out: RouteServerBgpStatus = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.route_server_bgp_state

        out["status"] = aws_sdk_ec2.types.route_server_bgp_state.deserialize_ec2_query(
            child_status
        )
    return out
