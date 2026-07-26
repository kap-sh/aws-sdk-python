"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteAssertionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.uuid


class DeleteAssertionResponse(TypedDict, closed=True):
    assertion_id: NotRequired["capo_resiliencehubv2.types.uuid.Uuid"]
    """<p>The unique identifier of the deleted assertion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssertionResponse) -> dict:
    out: dict = {}
    if "assertion_id" in value:
        out["assertionId"] = value["assertion_id"]
    return out


def deserialize_json(data: dict) -> DeleteAssertionResponse:
    out: DeleteAssertionResponse = {}  # type: ignore[typeddict-item]
    if "assertionId" in data:
        out["assertion_id"] = data["assertionId"]
    return out
