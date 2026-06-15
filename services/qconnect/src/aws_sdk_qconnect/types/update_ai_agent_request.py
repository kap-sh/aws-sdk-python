"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateAIAgentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_agent_configuration
    import aws_sdk_qconnect.types.client_token
    import aws_sdk_qconnect.types.description
    import aws_sdk_qconnect.types.uuid_or_arn
    import aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier
    import aws_sdk_qconnect.types.visibility_status


class UpdateAIAgentRequest(TypedDict):
    client_token: NotRequired["aws_sdk_qconnect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>..</p>"""
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    ai_agent_id: "aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the Amazon Q in Connect AI Agent.</p>"""
    visibility_status: "aws_sdk_qconnect.types.visibility_status.VisibilityStatus"
    """<p>The visbility status of the Amazon Q in Connect AI Agent.</p>"""
    configuration: NotRequired[
        "aws_sdk_qconnect.types.ai_agent_configuration.AIAgentConfiguration"
    ]
    """<p>The configuration of the Amazon Q in Connect AI Agent.</p>"""
    description: NotRequired["aws_sdk_qconnect.types.description.Description"]
    """<p>The description of the Amazon Q in Connect AI Agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAIAgentRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["visibilityStatus"] = value["visibility_status"]
    if "configuration" in value:
        import aws_sdk_qconnect.types.ai_agent_configuration

        out["configuration"] = (
            aws_sdk_qconnect.types.ai_agent_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateAIAgentRequest:
    out: UpdateAIAgentRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "visibilityStatus" in data:
        out["visibility_status"] = data["visibilityStatus"]
    else:
        raise DeserializationError("UpdateAIAgentRequest.visibility_status required")
    if "configuration" in data:
        import aws_sdk_qconnect.types.ai_agent_configuration

        out["configuration"] = (
            aws_sdk_qconnect.types.ai_agent_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
