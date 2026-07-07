"""Generated from Smithy shape ``com.amazonaws.apigateway#GetUsagePlansRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.nullable_integer
    import aws_sdk_api_gateway.types.string


class GetUsagePlansRequest(TypedDict, closed=True):
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""
    key_id: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The identifier of the API key associated with the usage plans.</p>"""
    limit: NotRequired["aws_sdk_api_gateway.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUsagePlansRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUsagePlansRequest:
    out: GetUsagePlansRequest = {}  # type: ignore[typeddict-item]
    return out
