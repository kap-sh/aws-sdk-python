"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerBgpStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_bgp_state


class RouteServerBgpStatus(TypedDict, closed=True):
    status: NotRequired["capo_ec2.types.route_server_bgp_state.RouteServerBgpState"]
    """<p>The operational status of the BGP session. The status enables you to monitor session liveness if you lack monitoring on your router/appliance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerBgpStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status" in value:
        import capo_ec2.types.route_server_bgp_state

        capo_ec2.types.route_server_bgp_state.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )


def deserialize_ec2_query(el: Element) -> RouteServerBgpStatus:
    out: RouteServerBgpStatus = {}  # type: ignore[typeddict-item]
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.route_server_bgp_state

        out["status"] = capo_ec2.types.route_server_bgp_state.deserialize_ec2_query(
            child_status
        )
    return out
