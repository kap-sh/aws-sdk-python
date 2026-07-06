"""Generated from Smithy shape ``com.amazonaws.apigateway#GetApiKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.nullable_boolean
    import aws_sdk_api_gateway.types.nullable_integer
    import aws_sdk_api_gateway.types.string


class GetApiKeysRequest(TypedDict, closed=True):
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""
    limit: NotRequired["aws_sdk_api_gateway.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>"""
    name_query: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The name of queried API keys.</p>"""
    customer_id: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The identifier of a customer in Amazon Web Services Marketplace or an external system, such as a developer portal.</p>"""
    include_values: NotRequired[
        "aws_sdk_api_gateway.types.nullable_boolean.NullableBoolean"
    ]
    """<p>A boolean flag to specify whether (<code>true</code>) or not (<code>false</code>) the result contains key values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApiKeysRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApiKeysRequest:
    out: GetApiKeysRequest = {}  # type: ignore[typeddict-item]
    return out
