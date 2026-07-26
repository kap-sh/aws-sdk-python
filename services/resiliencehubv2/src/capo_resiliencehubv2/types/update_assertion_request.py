"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateAssertionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.assertion_text
    import capo_resiliencehubv2.types.uuid


class UpdateAssertionRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    assertion_id: "capo_resiliencehubv2.types.uuid.Uuid"
    """<p>The unique identifier of the assertion to update.</p>"""
    text: NotRequired["capo_resiliencehubv2.types.assertion_text.AssertionText"]
    """<p>The updated text content of the assertion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssertionRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["assertionId"] = value["assertion_id"]
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> UpdateAssertionRequest:
    out: UpdateAssertionRequest = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("UpdateAssertionRequest.service_arn required")
    if "assertionId" in data:
        out["assertion_id"] = data["assertionId"]
    else:
        raise DeserializationError("UpdateAssertionRequest.assertion_id required")
    if "text" in data:
        out["text"] = data["text"]
    return out
