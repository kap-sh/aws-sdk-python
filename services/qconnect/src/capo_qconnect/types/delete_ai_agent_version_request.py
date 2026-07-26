"""Generated from Smithy shape ``com.amazonaws.qconnect#DeleteAIAgentVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.uuid_or_arn_or_either_with_qualifier
    import capo_qconnect.types.version


class DeleteAIAgentVersionRequest(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    ai_agent_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the Amazon Q in Connect AI Agent. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    version_number: "capo_qconnect.types.version.Version"
    """<p>The version number of the AI Agent version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAIAgentVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAIAgentVersionRequest:
    out: DeleteAIAgentVersionRequest = {}  # type: ignore[typeddict-item]
    return out
