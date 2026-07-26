"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayLogging``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_gateway_access_log


class VirtualGatewayLogging(TypedDict, closed=True):
    access_log: NotRequired[
        "capo_app_mesh.types.virtual_gateway_access_log.VirtualGatewayAccessLog"
    ]
    """<p>The access log configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayLogging) -> dict:
    out: dict = {}
    if "access_log" in value:
        import capo_app_mesh.types.virtual_gateway_access_log

        out["accessLog"] = (
            capo_app_mesh.types.virtual_gateway_access_log.serialize_json(
                value["access_log"]
            )
        )
    return out


def deserialize_json(data: dict) -> VirtualGatewayLogging:
    out: VirtualGatewayLogging = {}  # type: ignore[typeddict-item]
    if "accessLog" in data:
        import capo_app_mesh.types.virtual_gateway_access_log

        out["access_log"] = (
            capo_app_mesh.types.virtual_gateway_access_log.deserialize_json(
                data["accessLog"]
            )
        )
    return out
