"""Generated from Smithy shape ``com.amazonaws.appmesh#Logging``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.access_log


class Logging(TypedDict, closed=True):
    access_log: NotRequired["capo_app_mesh.types.access_log.AccessLog"]
    """<p>The access log configuration for a virtual node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Logging) -> dict:
    out: dict = {}
    if "access_log" in value:
        import capo_app_mesh.types.access_log

        out["accessLog"] = capo_app_mesh.types.access_log.serialize_json(
            value["access_log"]
        )
    return out


def deserialize_json(data: dict) -> Logging:
    out: Logging = {}  # type: ignore[typeddict-item]
    if "accessLog" in data:
        import capo_app_mesh.types.access_log

        out["access_log"] = capo_app_mesh.types.access_log.deserialize_json(
            data["accessLog"]
        )
    return out
