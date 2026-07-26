"""Generated from Smithy shape ``com.amazonaws.qconnect#GetAssistantAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.uuid_or_arn


class GetAssistantAssociationRequest(TypedDict, closed=True):
    assistant_association_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the assistant association. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssistantAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssistantAssociationRequest:
    out: GetAssistantAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
