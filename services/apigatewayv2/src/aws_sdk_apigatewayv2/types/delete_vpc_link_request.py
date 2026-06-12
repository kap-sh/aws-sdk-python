"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeleteVpcLinkRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class DeleteVpcLinkRequest(TypedDict):
    vpc_link_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The ID of the VPC link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVpcLinkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVpcLinkRequest:
    out: DeleteVpcLinkRequest = {}  # type: ignore[typeddict-item]
    return out
