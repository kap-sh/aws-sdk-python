"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreateAgentSpaceInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_name
    import aws_sdk_devops_agent.types.description
    import aws_sdk_devops_agent.types.kms_key_arn
    import aws_sdk_devops_agent.types.locale
    import aws_sdk_devops_agent.types.tags


class CreateAgentSpaceInput(TypedDict):
    name: "aws_sdk_devops_agent.types.agent_space_name.AgentSpaceName"
    """<p>The name of the AgentSpace.</p>"""
    description: NotRequired["aws_sdk_devops_agent.types.description.Description"]
    """<p>The description of the AgentSpace.</p>"""
    locale: NotRequired["aws_sdk_devops_agent.types.locale.Locale"]
    """<p>The locale for the AgentSpace, which determines the language used in agent responses.</p>"""
    kms_key_arn: NotRequired["aws_sdk_devops_agent.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>"""
    client_token: NotRequired["str"]
    """<p>Client-provided token to ensure request idempotency. When the same token is provided in subsequent calls, the same response is returned within a 8-hour window.</p>"""
    tags: NotRequired["aws_sdk_devops_agent.types.tags.Tags"]
    """<p>Tags to add to the AgentSpace at creation time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentSpaceInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "locale" in value:
        out["locale"] = value["locale"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_devops_agent.types.tags

        out["tags"] = aws_sdk_devops_agent.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAgentSpaceInput:
    out: CreateAgentSpaceInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAgentSpaceInput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "locale" in data:
        out["locale"] = data["locale"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_devops_agent.types.tags

        out["tags"] = aws_sdk_devops_agent.types.tags.deserialize_json(data["tags"])
    return out
