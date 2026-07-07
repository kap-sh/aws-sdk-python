"""Generated from Smithy shape ``com.amazonaws.qconnect#DeleteAIPromptVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.uuid_or_arn
    import aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier
    import aws_sdk_qconnect.types.version


class DeleteAIPromptVersionRequest(TypedDict, closed=True):
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    ai_prompt_id: "aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the Amazon Q in Connect AI prompt.</p>"""
    version_number: "aws_sdk_qconnect.types.version.Version"
    """<p>The version number of the AI Prompt version to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAIPromptVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAIPromptVersionRequest:
    out: DeleteAIPromptVersionRequest = {}  # type: ignore[typeddict-item]
    return out
