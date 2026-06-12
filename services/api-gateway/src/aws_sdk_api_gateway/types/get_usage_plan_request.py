"""Generated from Smithy shape ``com.amazonaws.apigateway#GetUsagePlanRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class GetUsagePlanRequest(TypedDict):
    usage_plan_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The identifier of the UsagePlan resource to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUsagePlanRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUsagePlanRequest:
    out: GetUsagePlanRequest = {}  # type: ignore[typeddict-item]
    return out
