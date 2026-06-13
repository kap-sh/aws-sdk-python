"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_status_code


class VirtualGatewayStatus(TypedDict):
    status: (
        "aws_sdk_app_mesh.types.virtual_gateway_status_code.VirtualGatewayStatusCode"
    )
    """<p>The current status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayStatus) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> VirtualGatewayStatus:
    out: VirtualGatewayStatus = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("VirtualGatewayStatus.status required")
    return out
