"""Generated from Smithy shape ``com.amazonaws.apigateway#GetVpcLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class GetVpcLinkRequest(TypedDict, closed=True):
    vpc_link_id: "capo_api_gateway.types.string.String"
    """<p>The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVpcLinkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVpcLinkRequest:
    out: GetVpcLinkRequest = {}  # type: ignore[typeddict-item]
    return out
