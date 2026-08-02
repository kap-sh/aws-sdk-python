"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteRouteServerResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server


class DeleteRouteServerResult(TypedDict, closed=True):
    route_server: NotRequired["capo_ec2.types.route_server.RouteServer"]
    """<p>Information about the deleted route server.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteRouteServerResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "route_server" in value:
        import capo_ec2.types.route_server

        capo_ec2.types.route_server.serialize_ec2_query(
            value["route_server"], pairs, f"{key_prefix}RouteServer"
        )


def deserialize_ec2_query(el: Element) -> DeleteRouteServerResult:
    out: DeleteRouteServerResult = {}  # type: ignore[typeddict-item]
    child_route_server = el.find("RouteServer")
    if child_route_server is not None:
        import capo_ec2.types.route_server

        out["route_server"] = capo_ec2.types.route_server.deserialize_ec2_query(
            child_route_server
        )
    return out
