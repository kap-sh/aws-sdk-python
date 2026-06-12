"""Generated from Smithy shape ``com.amazonaws.apigateway#GetVpcLinksRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.nullable_integer
    import aws_sdk_api_gateway.types.string


class GetVpcLinksRequest(TypedDict):
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""
    limit: NotRequired["aws_sdk_api_gateway.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVpcLinksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVpcLinksRequest:
    out: GetVpcLinksRequest = {}  # type: ignore[typeddict-item]
    return out
