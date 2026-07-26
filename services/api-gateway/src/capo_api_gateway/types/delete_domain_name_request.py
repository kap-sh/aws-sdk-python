"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteDomainNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class DeleteDomainNameRequest(TypedDict, closed=True):
    domain_name: "capo_api_gateway.types.string.String"
    """<p>The name of the DomainName resource to be deleted.</p>"""
    domain_name_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p> The identifier for the domain name resource. Supported only for private custom domain names. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainNameRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainNameRequest:
    out: DeleteDomainNameRequest = {}  # type: ignore[typeddict-item]
    return out
