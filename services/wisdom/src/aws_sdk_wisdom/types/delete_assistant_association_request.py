"""Generated from Smithy shape ``com.amazonaws.wisdom#DeleteAssistantAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.uuid_or_arn


class DeleteAssistantAssociationRequest(TypedDict, closed=True):
    assistant_association_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the assistant association. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssistantAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssistantAssociationRequest:
    out: DeleteAssistantAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
