"""Generated from Smithy shape ``com.amazonaws.apigateway#GetUsageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.nullable_integer
    import aws_sdk_api_gateway.types.string


class GetUsageRequest(TypedDict):
    usage_plan_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The Id of the usage plan associated with the usage data.</p>"""
    key_id: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The Id of the API key associated with the resultant usage data.</p>"""
    start_date: "aws_sdk_api_gateway.types.string.String"
    """<p>The starting date (e.g., 2016-01-01) of the usage data.</p>"""
    end_date: "aws_sdk_api_gateway.types.string.String"
    """<p>The ending date (e.g., 2016-12-31) of the usage data.</p>"""
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""
    limit: NotRequired["aws_sdk_api_gateway.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUsageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUsageRequest:
    out: GetUsageRequest = {}  # type: ignore[typeddict-item]
    return out
