"""Generated from Smithy shape ``com.amazonaws.apigateway#GetUsagePlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class GetUsagePlanRequest(TypedDict, closed=True):
    usage_plan_id: "capo_api_gateway.types.string.String"
    """<p>The identifier of the UsagePlan resource to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUsagePlanRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUsagePlanRequest:
    out: GetUsagePlanRequest = {}  # type: ignore[typeddict-item]
    return out
