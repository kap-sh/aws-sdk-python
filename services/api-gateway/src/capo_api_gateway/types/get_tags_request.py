"""Generated from Smithy shape ``com.amazonaws.apigateway#GetTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.nullable_integer
    import capo_api_gateway.types.string


class GetTagsRequest(TypedDict, closed=True):
    resource_arn: "capo_api_gateway.types.string.String"
    """<p>The ARN of a resource that can be tagged.</p>"""
    position: NotRequired["capo_api_gateway.types.string.String"]
    """<p>(Not currently supported) The current pagination position in the paged result set.</p>"""
    limit: NotRequired["capo_api_gateway.types.nullable_integer.NullableInteger"]
    """<p>(Not currently supported) The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTagsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTagsRequest:
    out: GetTagsRequest = {}  # type: ignore[typeddict-item]
    return out
