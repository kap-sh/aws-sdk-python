"""Generated from Smithy shape ``com.amazonaws.qconnect#DeleteContentAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.uuid_or_arn


class DeleteContentAssociationRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base.</p>"""
    content_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the content.</p>"""
    content_association_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the content association. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteContentAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteContentAssociationRequest:
    out: DeleteContentAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
