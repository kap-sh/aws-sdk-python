"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetResourceGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.resource_gateway_identifier


class GetResourceGatewayRequest(TypedDict, closed=True):
    resource_gateway_identifier: "aws_sdk_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
    """<p>The ID of the resource gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourceGatewayRequest:
    out: GetResourceGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
