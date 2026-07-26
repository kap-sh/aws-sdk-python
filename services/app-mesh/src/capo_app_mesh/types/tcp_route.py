"""Generated from Smithy shape ``com.amazonaws.appmesh#TcpRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.tcp_route_action
    import capo_app_mesh.types.tcp_route_match
    import capo_app_mesh.types.tcp_timeout


class TcpRoute(TypedDict, closed=True):
    action: "capo_app_mesh.types.tcp_route_action.TcpRouteAction"
    """<p>The action to take if a match is determined.</p>"""
    timeout: NotRequired["capo_app_mesh.types.tcp_timeout.TcpTimeout"]
    """<p>An object that represents types of timeouts. </p>"""
    match: NotRequired["capo_app_mesh.types.tcp_route_match.TcpRouteMatch"]
    """<p>An object that represents the criteria for determining a request match.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TcpRoute) -> dict:
    out: dict = {}
    import capo_app_mesh.types.tcp_route_action

    out["action"] = capo_app_mesh.types.tcp_route_action.serialize_json(value["action"])
    if "timeout" in value:
        import capo_app_mesh.types.tcp_timeout

        out["timeout"] = capo_app_mesh.types.tcp_timeout.serialize_json(
            value["timeout"]
        )
    if "match" in value:
        import capo_app_mesh.types.tcp_route_match

        out["match"] = capo_app_mesh.types.tcp_route_match.serialize_json(
            value["match"]
        )
    return out


def deserialize_json(data: dict) -> TcpRoute:
    out: TcpRoute = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import capo_app_mesh.types.tcp_route_action

        out["action"] = capo_app_mesh.types.tcp_route_action.deserialize_json(
            data["action"]
        )
    else:
        raise DeserializationError("TcpRoute.action required")
    if "timeout" in data:
        import capo_app_mesh.types.tcp_timeout

        out["timeout"] = capo_app_mesh.types.tcp_timeout.deserialize_json(
            data["timeout"]
        )
    if "match" in data:
        import capo_app_mesh.types.tcp_route_match

        out["match"] = capo_app_mesh.types.tcp_route_match.deserialize_json(
            data["match"]
        )
    return out
