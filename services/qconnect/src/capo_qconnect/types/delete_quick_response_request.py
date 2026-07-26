"""Generated from Smithy shape ``com.amazonaws.qconnect#DeleteQuickResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.uuid_or_arn


class DeleteQuickResponseRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The knowledge base from which the quick response is deleted. The identifier of the knowledge base.</p>"""
    quick_response_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the quick response to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQuickResponseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQuickResponseRequest:
    out: DeleteQuickResponseRequest = {}  # type: ignore[typeddict-item]
    return out
