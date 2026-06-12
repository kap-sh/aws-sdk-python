"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteResourceGatewayResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.resource_gateway_arn
    import aws_sdk_vpc_lattice.types.resource_gateway_id
    import aws_sdk_vpc_lattice.types.resource_gateway_name
    import aws_sdk_vpc_lattice.types.resource_gateway_status


class DeleteResourceGatewayResponse(TypedDict):
    id: NotRequired["aws_sdk_vpc_lattice.types.resource_gateway_id.ResourceGatewayId"]
    """<p>The ID of the resource gateway.</p>"""
    arn: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_gateway_arn.ResourceGatewayArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource gateway.</p>"""
    name: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_gateway_name.ResourceGatewayName"
    ]
    """<p>The name of the resource gateway.</p>"""
    status: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_gateway_status.ResourceGatewayStatus"
    ]
    """<p>The status of the resource gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourceGatewayResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> DeleteResourceGatewayResponse:
    out: DeleteResourceGatewayResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    return out
