"""Generated from Smithy shape ``com.amazonaws.apigateway#GetBasePathMappingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.nullable_integer
    import capo_api_gateway.types.string


class GetBasePathMappingsRequest(TypedDict, closed=True):
    domain_name: "capo_api_gateway.types.string.String"
    """<p>The domain name of a BasePathMapping resource.</p>"""
    domain_name_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p> The identifier for the domain name resource. Supported only for private custom domain names. </p>"""
    position: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""
    limit: NotRequired["capo_api_gateway.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBasePathMappingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBasePathMappingsRequest:
    out: GetBasePathMappingsRequest = {}  # type: ignore[typeddict-item]
    return out
