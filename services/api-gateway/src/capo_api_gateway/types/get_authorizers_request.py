"""Generated from Smithy shape ``com.amazonaws.apigateway#GetAuthorizersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.nullable_integer
    import capo_api_gateway.types.string


class GetAuthorizersRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    position: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""
    limit: NotRequired["capo_api_gateway.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAuthorizersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAuthorizersRequest:
    out: GetAuthorizersRequest = {}  # type: ignore[typeddict-item]
    return out
