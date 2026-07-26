"""Generated from Smithy shape ``com.amazonaws.qconnect#GetMessageTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.uuid_or_arn_or_either_with_qualifier


class GetMessageTemplateRequest(TypedDict, closed=True):
    message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the message template. Can be either the ID or the ARN.</p>"""
    knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMessageTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMessageTemplateRequest:
    out: GetMessageTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
