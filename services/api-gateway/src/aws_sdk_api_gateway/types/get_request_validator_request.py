"""Generated from Smithy shape ``com.amazonaws.apigateway#GetRequestValidatorRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class GetRequestValidatorRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    request_validator_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The identifier of the RequestValidator to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRequestValidatorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRequestValidatorRequest:
    out: GetRequestValidatorRequest = {}  # type: ignore[typeddict-item]
    return out
