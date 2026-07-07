"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteResourceGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.resource_gateway_identifier


class DeleteResourceGatewayRequest(TypedDict, closed=True):
    resource_gateway_identifier: "aws_sdk_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
    """<p>The ID or ARN of the resource gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourceGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourceGatewayRequest:
    out: DeleteResourceGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
