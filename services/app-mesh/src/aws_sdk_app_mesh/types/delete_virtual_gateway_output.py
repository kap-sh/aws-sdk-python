"""Generated from Smithy shape ``com.amazonaws.appmesh#DeleteVirtualGatewayOutput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_app_mesh.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_data

class DeleteVirtualGatewayOutput(TypedDict):
    virtual_gateway: "aws_sdk_app_mesh.types.virtual_gateway_data.VirtualGatewayData"
    """<p>The virtual gateway that was deleted.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteVirtualGatewayOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.virtual_gateway_data
    out["virtualGateway"] = aws_sdk_app_mesh.types.virtual_gateway_data.serialize_json(value["virtual_gateway"])
    return out


def deserialize_json(data: dict) -> DeleteVirtualGatewayOutput:
    out: DeleteVirtualGatewayOutput = {}  # type: ignore[typeddict-item]
    if "virtualGateway" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_data
        out["virtual_gateway"] = aws_sdk_app_mesh.types.virtual_gateway_data.deserialize_json(data["virtualGateway"])
    else:
        raise DeserializationError("DeleteVirtualGatewayOutput.virtual_gateway required")
    return out