"""Generated from Smithy shape ``com.amazonaws.appmesh#TcpTimeout``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.duration


class TcpTimeout(TypedDict):
    idle: NotRequired["aws_sdk_app_mesh.types.duration.Duration"]
    """<p>An object that represents an idle timeout. An idle timeout bounds the amount of time that a connection may be idle. The default value is none.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TcpTimeout) -> dict:
    out: dict = {}
    if "idle" in value:
        import aws_sdk_app_mesh.types.duration

        out["idle"] = aws_sdk_app_mesh.types.duration.serialize_json(value["idle"])
    return out


def deserialize_json(data: dict) -> TcpTimeout:
    out: TcpTimeout = {}  # type: ignore[typeddict-item]
    if "idle" in data:
        import aws_sdk_app_mesh.types.duration

        out["idle"] = aws_sdk_app_mesh.types.duration.deserialize_json(data["idle"])
    return out
