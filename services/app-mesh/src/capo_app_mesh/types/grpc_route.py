"""Generated from Smithy shape ``com.amazonaws.appmesh#GrpcRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.grpc_retry_policy
    import capo_app_mesh.types.grpc_route_action
    import capo_app_mesh.types.grpc_route_match
    import capo_app_mesh.types.grpc_timeout


class GrpcRoute(TypedDict, closed=True):
    action: "capo_app_mesh.types.grpc_route_action.GrpcRouteAction"
    """<p>An object that represents the action to take if a match is determined.</p>"""
    match: "capo_app_mesh.types.grpc_route_match.GrpcRouteMatch"
    """<p>An object that represents the criteria for determining a request match.</p>"""
    retry_policy: NotRequired["capo_app_mesh.types.grpc_retry_policy.GrpcRetryPolicy"]
    """<p>An object that represents a retry policy.</p>"""
    timeout: NotRequired["capo_app_mesh.types.grpc_timeout.GrpcTimeout"]
    """<p>An object that represents types of timeouts. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrpcRoute) -> dict:
    out: dict = {}
    import capo_app_mesh.types.grpc_route_action

    out["action"] = capo_app_mesh.types.grpc_route_action.serialize_json(
        value["action"]
    )
    import capo_app_mesh.types.grpc_route_match

    out["match"] = capo_app_mesh.types.grpc_route_match.serialize_json(value["match"])
    if "retry_policy" in value:
        import capo_app_mesh.types.grpc_retry_policy

        out["retryPolicy"] = capo_app_mesh.types.grpc_retry_policy.serialize_json(
            value["retry_policy"]
        )
    if "timeout" in value:
        import capo_app_mesh.types.grpc_timeout

        out["timeout"] = capo_app_mesh.types.grpc_timeout.serialize_json(
            value["timeout"]
        )
    return out


def deserialize_json(data: dict) -> GrpcRoute:
    out: GrpcRoute = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import capo_app_mesh.types.grpc_route_action

        out["action"] = capo_app_mesh.types.grpc_route_action.deserialize_json(
            data["action"]
        )
    else:
        raise DeserializationError("GrpcRoute.action required")
    if "match" in data:
        import capo_app_mesh.types.grpc_route_match

        out["match"] = capo_app_mesh.types.grpc_route_match.deserialize_json(
            data["match"]
        )
    else:
        raise DeserializationError("GrpcRoute.match required")
    if "retryPolicy" in data:
        import capo_app_mesh.types.grpc_retry_policy

        out["retry_policy"] = capo_app_mesh.types.grpc_retry_policy.deserialize_json(
            data["retryPolicy"]
        )
    if "timeout" in data:
        import capo_app_mesh.types.grpc_timeout

        out["timeout"] = capo_app_mesh.types.grpc_timeout.deserialize_json(
            data["timeout"]
        )
    return out
