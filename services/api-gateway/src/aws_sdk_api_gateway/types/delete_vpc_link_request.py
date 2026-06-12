"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteVpcLinkRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class DeleteVpcLinkRequest(TypedDict):
    vpc_link_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVpcLinkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVpcLinkRequest:
    out: DeleteVpcLinkRequest = {}  # type: ignore[typeddict-item]
    return out
