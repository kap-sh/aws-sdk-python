"""Generated from Smithy shape ``com.amazonaws.apigateway#GetUsagePlanKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class GetUsagePlanKeyRequest(TypedDict, closed=True):
    usage_plan_id: "capo_api_gateway.types.string.String"
    """<p>The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer.</p>"""
    key_id: "capo_api_gateway.types.string.String"
    """<p>The key Id of the to-be-retrieved UsagePlanKey resource representing a plan customer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUsagePlanKeyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUsagePlanKeyRequest:
    out: GetUsagePlanKeyRequest = {}  # type: ignore[typeddict-item]
    return out
