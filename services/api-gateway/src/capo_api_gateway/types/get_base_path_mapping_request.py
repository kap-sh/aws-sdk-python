"""Generated from Smithy shape ``com.amazonaws.apigateway#GetBasePathMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class GetBasePathMappingRequest(TypedDict, closed=True):
    domain_name: "capo_api_gateway.types.string.String"
    """<p>The domain name of the BasePathMapping resource to be described.</p>"""
    domain_name_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The identifier for the domain name resource. Supported only for private custom domain names. </p>"""
    base_path: "capo_api_gateway.types.string.String"
    """<p>The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Specify '(none)' if you do not want callers to specify any base path name after the domain name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBasePathMappingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBasePathMappingRequest:
    out: GetBasePathMappingRequest = {}  # type: ignore[typeddict-item]
    return out
