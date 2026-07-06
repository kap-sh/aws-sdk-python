"""Generated from Smithy shape ``com.amazonaws.qconnect#GetContentAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.uuid_or_arn


class GetContentAssociationRequest(TypedDict, closed=True):
    knowledge_base_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base.</p>"""
    content_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the content.</p>"""
    content_association_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the content association. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContentAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetContentAssociationRequest:
    out: GetContentAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
