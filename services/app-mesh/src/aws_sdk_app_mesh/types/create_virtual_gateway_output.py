"""Generated from Smithy shape ``com.amazonaws.appmesh#CreateVirtualGatewayOutput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_app_mesh.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_data

class CreateVirtualGatewayOutput(TypedDict):
    virtual_gateway: "aws_sdk_app_mesh.types.virtual_gateway_data.VirtualGatewayData"
    """<p>The full description of your virtual gateway following the create call.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateVirtualGatewayOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.virtual_gateway_data
    out["virtualGateway"] = aws_sdk_app_mesh.types.virtual_gateway_data.serialize_json(value["virtual_gateway"])
    return out


def deserialize_json(data: dict) -> CreateVirtualGatewayOutput:
    out: CreateVirtualGatewayOutput = {}  # type: ignore[typeddict-item]
    if "virtualGateway" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_data
        out["virtual_gateway"] = aws_sdk_app_mesh.types.virtual_gateway_data.deserialize_json(data["virtualGateway"])
    else:
        raise DeserializationError("CreateVirtualGatewayOutput.virtual_gateway required")
    return out