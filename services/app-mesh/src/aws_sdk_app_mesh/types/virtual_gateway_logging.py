"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayLogging``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_access_log


class VirtualGatewayLogging(TypedDict):
    access_log: NotRequired[
        "aws_sdk_app_mesh.types.virtual_gateway_access_log.VirtualGatewayAccessLog"
    ]
    """<p>The access log configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayLogging) -> dict:
    out: dict = {}
    if "access_log" in value:
        import aws_sdk_app_mesh.types.virtual_gateway_access_log

        out["accessLog"] = (
            aws_sdk_app_mesh.types.virtual_gateway_access_log.serialize_json(
                value["access_log"]
            )
        )
    return out


def deserialize_json(data: dict) -> VirtualGatewayLogging:
    out: VirtualGatewayLogging = {}  # type: ignore[typeddict-item]
    if "accessLog" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_access_log

        out["access_log"] = (
            aws_sdk_app_mesh.types.virtual_gateway_access_log.deserialize_json(
                data["accessLog"]
            )
        )
    return out
