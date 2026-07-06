"""Generated from Smithy shape ``com.amazonaws.qconnect#OrchestratorConfigurationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.non_empty_string
    import aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier


class OrchestratorConfigurationEntry(TypedDict, closed=True):
    ai_agent_id: NotRequired[
        "aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    ]
    """<p>The identifier of the AI Agent in the orchestrator configuration.</p>"""
    orchestrator_use_case: "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The use case for the orchestrator configuration. (for example Connect.SelfService, Connect.AgentAssistance)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrchestratorConfigurationEntry) -> dict:
    out: dict = {}
    if "ai_agent_id" in value:
        out["aiAgentId"] = value["ai_agent_id"]
    out["orchestratorUseCase"] = value["orchestrator_use_case"]
    return out


def deserialize_json(data: dict) -> OrchestratorConfigurationEntry:
    out: OrchestratorConfigurationEntry = {}  # type: ignore[typeddict-item]
    if "aiAgentId" in data:
        out["ai_agent_id"] = data["aiAgentId"]
    if "orchestratorUseCase" in data:
        out["orchestrator_use_case"] = data["orchestratorUseCase"]
    else:
        raise DeserializationError(
            "OrchestratorConfigurationEntry.orchestrator_use_case required"
        )
    return out
