"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteUsagePlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class DeleteUsagePlanRequest(TypedDict, closed=True):
    usage_plan_id: "capo_api_gateway.types.string.String"
    """<p>The Id of the to-be-deleted usage plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUsagePlanRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteUsagePlanRequest:
    out: DeleteUsagePlanRequest = {}  # type: ignore[typeddict-item]
    return out
