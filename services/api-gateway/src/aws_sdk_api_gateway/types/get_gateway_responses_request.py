"""Generated from Smithy shape ``com.amazonaws.apigateway#GetGatewayResponsesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.nullable_integer
    import aws_sdk_api_gateway.types.string


class GetGatewayResponsesRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set. The GatewayResponse collection does not support pagination and the position does not apply here.</p>"""
    limit: NotRequired["aws_sdk_api_gateway.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500. The GatewayResponses collection does not support pagination and the limit does not apply here.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGatewayResponsesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGatewayResponsesRequest:
    out: GetGatewayResponsesRequest = {}  # type: ignore[typeddict-item]
    return out
