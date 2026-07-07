"""Generated from Smithy shape ``com.amazonaws.apigateway#GetUsagePlanKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.nullable_integer
    import aws_sdk_api_gateway.types.string


class GetUsagePlanKeysRequest(TypedDict, closed=True):
    usage_plan_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer.</p>"""
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""
    limit: NotRequired["aws_sdk_api_gateway.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>"""
    name_query: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>A query parameter specifying the name of the to-be-returned usage plan keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUsagePlanKeysRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUsagePlanKeysRequest:
    out: GetUsagePlanKeysRequest = {}  # type: ignore[typeddict-item]
    return out
