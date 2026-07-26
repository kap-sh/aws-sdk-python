"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteServiceFunctionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.entity_id


class DeleteServiceFunctionResponse(TypedDict, closed=True):
    service_function_id: NotRequired["capo_resiliencehubv2.types.entity_id.EntityId"]
    """<p>The identifier of the deleted service function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceFunctionResponse) -> dict:
    out: dict = {}
    if "service_function_id" in value:
        out["serviceFunctionId"] = value["service_function_id"]
    return out


def deserialize_json(data: dict) -> DeleteServiceFunctionResponse:
    out: DeleteServiceFunctionResponse = {}  # type: ignore[typeddict-item]
    if "serviceFunctionId" in data:
        out["service_function_id"] = data["serviceFunctionId"]
    return out
