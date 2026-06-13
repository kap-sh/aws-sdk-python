"""Generated from Smithy shape ``com.amazonaws.appmesh#UpdateVirtualGatewayOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_data


class UpdateVirtualGatewayOutput(TypedDict):
    virtual_gateway: "aws_sdk_app_mesh.types.virtual_gateway_data.VirtualGatewayData"
    """<p>A full description of the virtual gateway that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVirtualGatewayOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.virtual_gateway_data

    out["virtualGateway"] = aws_sdk_app_mesh.types.virtual_gateway_data.serialize_json(
        value["virtual_gateway"]
    )
    return out


def deserialize_json(data: dict) -> UpdateVirtualGatewayOutput:
    out: UpdateVirtualGatewayOutput = {}  # type: ignore[typeddict-item]
    if "virtualGateway" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_data

        out["virtual_gateway"] = (
            aws_sdk_app_mesh.types.virtual_gateway_data.deserialize_json(
                data["virtualGateway"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateVirtualGatewayOutput.virtual_gateway required"
        )
    return out
