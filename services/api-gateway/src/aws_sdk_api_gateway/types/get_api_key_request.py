"""Generated from Smithy shape ``com.amazonaws.apigateway#GetApiKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.nullable_boolean
    import aws_sdk_api_gateway.types.string


class GetApiKeyRequest(TypedDict, closed=True):
    api_key: "aws_sdk_api_gateway.types.string.String"
    """<p>The identifier of the ApiKey resource.</p>"""
    include_value: NotRequired[
        "aws_sdk_api_gateway.types.nullable_boolean.NullableBoolean"
    ]
    """<p>A boolean flag to specify whether (<code>true</code>) or not (<code>false</code>) the result contains the key value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApiKeyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApiKeyRequest:
    out: GetApiKeyRequest = {}  # type: ignore[typeddict-item]
    return out
