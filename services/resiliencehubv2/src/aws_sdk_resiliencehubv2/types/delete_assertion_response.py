"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteAssertionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.uuid


class DeleteAssertionResponse(TypedDict):
    assertion_id: NotRequired["aws_sdk_resiliencehubv2.types.uuid.Uuid"]
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
