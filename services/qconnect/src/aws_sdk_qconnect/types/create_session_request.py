"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_agent_configuration_map
    import aws_sdk_qconnect.types.client_token
    import aws_sdk_qconnect.types.description
    import aws_sdk_qconnect.types.generic_arn
    import aws_sdk_qconnect.types.name
    import aws_sdk_qconnect.types.orchestrator_configuration_list
    import aws_sdk_qconnect.types.tag_filter
    import aws_sdk_qconnect.types.tags
    import aws_sdk_qconnect.types.uuid_or_arn


class CreateSessionRequest(TypedDict):
    client_token: NotRequired["aws_sdk_qconnect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    name: "aws_sdk_qconnect.types.name.Name"
    """<p>The name of the session.</p>"""
    description: NotRequired["aws_sdk_qconnect.types.description.Description"]
    """<p>The description.</p>"""
    tags: NotRequired["aws_sdk_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    tag_filter: NotRequired["aws_sdk_qconnect.types.tag_filter.TagFilter"]
    """<p>An object that can be used to specify Tag conditions. </p>"""
    ai_agent_configuration: NotRequired[
        "aws_sdk_qconnect.types.ai_agent_configuration_map.AIAgentConfigurationMap"
    ]
    """<p>The configuration of the AI Agents (mapped by AI Agent Type to AI Agent version) that should be used by Amazon Q in Connect for this Session.</p>"""
    contact_arn: NotRequired["aws_sdk_qconnect.types.generic_arn.GenericArn"]
    """<p>The Amazon Resource Name (ARN) of the email contact in Amazon Connect. Used to retrieve email content and establish session context for AI-powered email assistance.</p>"""
    orchestrator_configuration_list: NotRequired[
        "aws_sdk_qconnect.types.orchestrator_configuration_list.OrchestratorConfigurationList"
    ]
    """<p>The list of orchestrator configurations for the session being created.</p>"""
    remove_orchestrator_configuration_list: NotRequired["bool"]
    """<p>The list of orchestrator configurations to remove from the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSessionRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.serialize_json(value["tags"])
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
    if "contact_arn" in value:
        out["contactArn"] = value["contact_arn"]
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


def deserialize_json(data: dict) -> CreateSessionRequest:
    out: CreateSessionRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSessionRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.deserialize_json(data["tags"])
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
    if "contactArn" in data:
        out["contact_arn"] = data["contactArn"]
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
