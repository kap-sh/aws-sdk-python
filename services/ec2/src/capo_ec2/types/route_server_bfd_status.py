"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerBfdStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_bfd_state


class RouteServerBfdStatus(TypedDict, closed=True):
    status: NotRequired["capo_ec2.types.route_server_bfd_state.RouteServerBfdState"]
    """<p>The operational status of the BFD session.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerBfdStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status" in value:
        import capo_ec2.types.route_server_bfd_state

        capo_ec2.types.route_server_bfd_state.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )


def deserialize_ec2_query(el: Element) -> RouteServerBfdStatus:
    out: RouteServerBfdStatus = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_ec2.types.route_server_bfd_state

        out["status"] = capo_ec2.types.route_server_bfd_state.deserialize_ec2_query(
            child_status
        )
    return out
