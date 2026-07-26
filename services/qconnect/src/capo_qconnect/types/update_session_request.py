"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_agent_configuration_map
    import capo_qconnect.types.description
    import capo_qconnect.types.orchestrator_configuration_list
    import capo_qconnect.types.tag_filter
    import capo_qconnect.types.uuid_or_arn


class UpdateSessionRequest(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    description: NotRequired["capo_qconnect.types.description.Description"]
    """<p>The description.</p>"""
    tag_filter: NotRequired["capo_qconnect.types.tag_filter.TagFilter"]
    """<p>An object that can be used to specify Tag conditions.</p>"""
    ai_agent_configuration: NotRequired[
        "capo_qconnect.types.ai_agent_configuration_map.AIAgentConfigurationMap"
    ]
    """<p>The configuration of the AI Agents (mapped by AI Agent Type to AI Agent version) that should be used by Amazon Q in Connect for this Session.</p>"""
    orchestrator_configuration_list: NotRequired[
        "capo_qconnect.types.orchestrator_configuration_list.OrchestratorConfigurationList"
    ]
    """<p>The updated list of orchestrator configurations for the session.</p>"""
    remove_orchestrator_configuration_list: NotRequired["bool"]
    """<p>The list of orchestrator configurations to remove from the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSessionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "tag_filter" in value:
        import capo_qconnect.types.tag_filter

        out["tagFilter"] = capo_qconnect.types.tag_filter.serialize_json(
            value["tag_filter"]
        )
    if "ai_agent_configuration" in value:
        import capo_qconnect.types.ai_agent_configuration_map

        out["aiAgentConfiguration"] = (
            capo_qconnect.types.ai_agent_configuration_map.serialize_json(
                value["ai_agent_configuration"]
            )
        )
    if "orchestrator_configuration_list" in value:
        import capo_qconnect.types.orchestrator_configuration_list

        out["orchestratorConfigurationList"] = (
            capo_qconnect.types.orchestrator_configuration_list.serialize_json(
                value["orchestrator_configuration_list"]
            )
        )
    if "remove_orchestrator_configuration_list" in value:
        out["removeOrchestratorConfigurationList"] = value[
            "remove_orchestrator_configuration_list"
        ]
    return out


def deserialize_json(data: dict) -> UpdateSessionRequest:
    out: UpdateSessionRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "tagFilter" in data:
        import capo_qconnect.types.tag_filter

        out["tag_filter"] = capo_qconnect.types.tag_filter.deserialize_json(
            data["tagFilter"]
        )
    if "aiAgentConfiguration" in data:
        import capo_qconnect.types.ai_agent_configuration_map

        out["ai_agent_configuration"] = (
            capo_qconnect.types.ai_agent_configuration_map.deserialize_json(
                data["aiAgentConfiguration"]
            )
        )
    if "orchestratorConfigurationList" in data:
        import capo_qconnect.types.orchestrator_configuration_list

        out["orchestrator_configuration_list"] = (
            capo_qconnect.types.orchestrator_configuration_list.deserialize_json(
                data["orchestratorConfigurationList"]
            )
        )
    if "removeOrchestratorConfigurationList" in data:
        out["remove_orchestrator_configuration_list"] = data[
            "removeOrchestratorConfigurationList"
        ]
    return out
