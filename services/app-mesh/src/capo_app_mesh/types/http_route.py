"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.http_retry_policy
    import capo_app_mesh.types.http_route_action
    import capo_app_mesh.types.http_route_match
    import capo_app_mesh.types.http_timeout


class HttpRoute(TypedDict, closed=True):
    match: "capo_app_mesh.types.http_route_match.HttpRouteMatch"
    """<p>An object that represents the criteria for determining a request match.</p>"""
    action: "capo_app_mesh.types.http_route_action.HttpRouteAction"
    """<p>An object that represents the action to take if a match is determined.</p>"""
    retry_policy: NotRequired["capo_app_mesh.types.http_retry_policy.HttpRetryPolicy"]
    """<p>An object that represents a retry policy.</p>"""
    timeout: NotRequired["capo_app_mesh.types.http_timeout.HttpTimeout"]
    """<p>An object that represents types of timeouts. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpRoute) -> dict:
    out: dict = {}
    import capo_app_mesh.types.http_route_match

    out["match"] = capo_app_mesh.types.http_route_match.serialize_json(value["match"])
    import capo_app_mesh.types.http_route_action

    out["action"] = capo_app_mesh.types.http_route_action.serialize_json(
        value["action"]
    )
    if "retry_policy" in value:
        import capo_app_mesh.types.http_retry_policy

        out["retryPolicy"] = capo_app_mesh.types.http_retry_policy.serialize_json(
            value["retry_policy"]
        )
    if "timeout" in value:
        import capo_app_mesh.types.http_timeout

        out["timeout"] = capo_app_mesh.types.http_timeout.serialize_json(
            value["timeout"]
        )
    return out


def deserialize_json(data: dict) -> HttpRoute:
    out: HttpRoute = {}  # type: ignore[typeddict-item]
    if "match" in data:
        import capo_app_mesh.types.http_route_match

        out["match"] = capo_app_mesh.types.http_route_match.deserialize_json(
            data["match"]
        )
    else:
        raise DeserializationError("HttpRoute.match required")
    if "action" in data:
        import capo_app_mesh.types.http_route_action

        out["action"] = capo_app_mesh.types.http_route_action.deserialize_json(
            data["action"]
        )
    else:
        raise DeserializationError("HttpRoute.action required")
    if "retryPolicy" in data:
        import capo_app_mesh.types.http_retry_policy

        out["retry_policy"] = capo_app_mesh.types.http_retry_policy.deserialize_json(
            data["retryPolicy"]
        )
    if "timeout" in data:
        import capo_app_mesh.types.http_timeout

        out["timeout"] = capo_app_mesh.types.http_timeout.deserialize_json(
            data["timeout"]
        )
    return out
