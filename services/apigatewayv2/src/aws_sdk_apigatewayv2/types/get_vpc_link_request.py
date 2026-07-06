"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetVpcLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class GetVpcLinkRequest(TypedDict, closed=True):
    vpc_link_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The ID of the VPC link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVpcLinkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVpcLinkRequest:
    out: GetVpcLinkRequest = {}  # type: ignore[typeddict-item]
    return out
