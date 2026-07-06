"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteBasePathMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class DeleteBasePathMappingRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_api_gateway.types.string.String"
    """<p>The domain name of the BasePathMapping resource to delete.</p>"""
    domain_name_id: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p> The identifier for the domain name resource. Supported only for private custom domain names. </p>"""
    base_path: "aws_sdk_api_gateway.types.string.String"
    """<p>The base path name of the BasePathMapping resource to delete.</p> <p>To specify an empty base path, set this parameter to <code>'(none)'</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBasePathMappingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBasePathMappingRequest:
    out: DeleteBasePathMappingRequest = {}  # type: ignore[typeddict-item]
    return out
