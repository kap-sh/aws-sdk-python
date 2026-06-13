"""Generated from Smithy shape ``com.amazonaws.appmesh#Logging``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.access_log


class Logging(TypedDict):
    access_log: NotRequired["aws_sdk_app_mesh.types.access_log.AccessLog"]
    """<p>The access log configuration for a virtual node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Logging) -> dict:
    out: dict = {}
    if "access_log" in value:
        import aws_sdk_app_mesh.types.access_log

        out["accessLog"] = aws_sdk_app_mesh.types.access_log.serialize_json(
            value["access_log"]
        )
    return out


def deserialize_json(data: dict) -> Logging:
    out: Logging = {}  # type: ignore[typeddict-item]
    if "accessLog" in data:
        import aws_sdk_app_mesh.types.access_log

        out["access_log"] = aws_sdk_app_mesh.types.access_log.deserialize_json(
            data["accessLog"]
        )
    return out
