"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpTimeout``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.duration


class HttpTimeout(TypedDict, closed=True):
    per_request: NotRequired["aws_sdk_app_mesh.types.duration.Duration"]
    """<p>An object that represents a per request timeout. The default value is 15 seconds. If you set a higher timeout, then make sure that the higher value is set for each App Mesh resource in a conversation. For example, if a virtual node backend uses a virtual router provider to route to another virtual node, then the timeout should be greater than 15 seconds for the source and destination virtual node and the route.</p>"""
    idle: NotRequired["aws_sdk_app_mesh.types.duration.Duration"]
    """<p>An object that represents an idle timeout. An idle timeout bounds the amount of time that a connection may be idle. The default value is none.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpTimeout) -> dict:
    out: dict = {}
    if "per_request" in value:
        import aws_sdk_app_mesh.types.duration

        out["perRequest"] = aws_sdk_app_mesh.types.duration.serialize_json(
            value["per_request"]
        )
    if "idle" in value:
        import aws_sdk_app_mesh.types.duration

        out["idle"] = aws_sdk_app_mesh.types.duration.serialize_json(value["idle"])
    return out


def deserialize_json(data: dict) -> HttpTimeout:
    out: HttpTimeout = {}  # type: ignore[typeddict-item]
    if "perRequest" in data:
        import aws_sdk_app_mesh.types.duration

        out["per_request"] = aws_sdk_app_mesh.types.duration.deserialize_json(
            data["perRequest"]
        )
    if "idle" in data:
        import aws_sdk_app_mesh.types.duration

        out["idle"] = aws_sdk_app_mesh.types.duration.deserialize_json(data["idle"])
    return out
