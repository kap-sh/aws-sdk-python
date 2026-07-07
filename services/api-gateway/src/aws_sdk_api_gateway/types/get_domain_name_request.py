"""Generated from Smithy shape ``com.amazonaws.apigateway#GetDomainNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class GetDomainNameRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_api_gateway.types.string.String"
    """<p>The name of the DomainName resource.</p>"""
    domain_name_id: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p> The identifier for the domain name resource. Required for private custom domain names. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainNameRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainNameRequest:
    out: GetDomainNameRequest = {}  # type: ignore[typeddict-item]
    return out
