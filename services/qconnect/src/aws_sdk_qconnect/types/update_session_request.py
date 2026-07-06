"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_agent_configuration_map
    import aws_sdk_qconnect.types.description
    import aws_sdk_qconnect.types.orchestrator_configuration_list
    import aws_sdk_qconnect.types.tag_filter
    import aws_sdk_qconnect.types.uuid_or_arn


class UpdateSessionRequest(TypedDict, closed=True):
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    session_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    description: NotRequired["aws_sdk_qconnect.types.description.Description"]
    """<p>The description.</p>"""
    tag_filter: NotRequired["aws_sdk_qconnect.types.tag_filter.TagFilter"]
    """<p>An object that can be used to specify Tag conditions.</p>"""
    ai_agent_configuration: NotRequired[
        "aws_sdk_qconnect.types.ai_agent_configuration_map.AIAgentConfigurationMap"
    ]
    """<p>The configuration of the AI Agents (mapped by AI Agent Type to AI Agent version) that should be used by Amazon Q in Connect for this Session.</p>"""
    orchestrator_configuration_list: NotRequired[
        "aws_sdk_qconnect.types.orchestrator_configuration_list.OrchestratorConfigurationList"
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
        import aws_sdk_qconnect.types.tag_filter

        out["tagFilter"] = aws_sdk_qconnect.types.tag_filter.serialize_json(
            value["tag_filter"]
        )
    if "ai_agent_configuration" in value:
        import aws_sdk_qconnect.types.ai_agent_configuration_map

        out["aiAgentConfiguration"] = (
            aws_sdk_qconnect.types.ai_agent_configuration_map.serialize_json(
                value["ai_agent_configuration"]
            )
        )
    if "orchestrator_configuration_list" in value:
        import aws_sdk_qconnect.types.orchestrator_configuration_list

        out["orchestratorConfigurationList"] = (
            aws_sdk_qconnect.types.orchestrator_configuration_list.serialize_json(
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
        import aws_sdk_qconnect.types.tag_filter

        out["tag_filter"] = aws_sdk_qconnect.types.tag_filter.deserialize_json(
            data["tagFilter"]
        )
    if "aiAgentConfiguration" in data:
        import aws_sdk_qconnect.types.ai_agent_configuration_map

        out["ai_agent_configuration"] = (
            aws_sdk_qconnect.types.ai_agent_configuration_map.deserialize_json(
                data["aiAgentConfiguration"]
            )
        )
    if "orchestratorConfigurationList" in data:
        import aws_sdk_qconnect.types.orchestrator_configuration_list

        out["orchestrator_configuration_list"] = (
            aws_sdk_qconnect.types.orchestrator_configuration_list.deserialize_json(
                data["orchestratorConfigurationList"]
            )
        )
    if "removeOrchestratorConfigurationList" in data:
        out["remove_orchestrator_configuration_list"] = data[
            "removeOrchestratorConfigurationList"
        ]
    return out
