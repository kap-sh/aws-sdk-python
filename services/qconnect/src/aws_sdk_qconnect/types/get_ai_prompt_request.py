"""Generated from Smithy shape ``com.amazonaws.qconnect#GetAIPromptRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.uuid_or_arn
    import aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier


class GetAIPromptRequest(TypedDict):
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    ai_prompt_id: "aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the Amazon Q in Connect AI prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAIPromptRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAIPromptRequest:
    out: GetAIPromptRequest = {}  # type: ignore[typeddict-item]
    return out
