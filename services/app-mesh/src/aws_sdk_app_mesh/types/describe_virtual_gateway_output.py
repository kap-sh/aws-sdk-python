"""Generated from Smithy shape ``com.amazonaws.appmesh#DescribeVirtualGatewayOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_data


class DescribeVirtualGatewayOutput(TypedDict, closed=True):
    virtual_gateway: "aws_sdk_app_mesh.types.virtual_gateway_data.VirtualGatewayData"
    """<p>The full description of your virtual gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVirtualGatewayOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.virtual_gateway_data

    out["virtualGateway"] = aws_sdk_app_mesh.types.virtual_gateway_data.serialize_json(
        value["virtual_gateway"]
    )
    return out


def deserialize_json(data: dict) -> DescribeVirtualGatewayOutput:
    out: DescribeVirtualGatewayOutput = {}  # type: ignore[typeddict-item]
    if "virtualGateway" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_data

        out["virtual_gateway"] = (
            aws_sdk_app_mesh.types.virtual_gateway_data.deserialize_json(
                data["virtualGateway"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeVirtualGatewayOutput.virtual_gateway required"
        )
    return out
