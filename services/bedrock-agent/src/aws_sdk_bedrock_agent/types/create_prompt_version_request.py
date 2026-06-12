"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreatePromptVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.client_token
    import aws_sdk_bedrock_agent.types.prompt_description
    import aws_sdk_bedrock_agent.types.prompt_identifier
    import aws_sdk_bedrock_agent.types.tags_map


class CreatePromptVersionRequest(TypedDict):
    prompt_identifier: "aws_sdk_bedrock_agent.types.prompt_identifier.PromptIdentifier"
    """<p>The unique identifier of the prompt that you want to create a version of.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agent.types.prompt_description.PromptDescription"
    ]
    """<p>A description for the version of the prompt.</p>"""
    client_token: NotRequired["aws_sdk_bedrock_agent.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>"""
    tags: NotRequired["aws_sdk_bedrock_agent.types.tags_map.TagsMap"]
    """<p>Any tags that you want to attach to the version of the prompt. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html\">Tagging resources in Amazon Bedrock</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePromptVersionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_bedrock_agent.types.tags_map

        out["tags"] = aws_sdk_bedrock_agent.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePromptVersionRequest:
    out: CreatePromptVersionRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_bedrock_agent.types.tags_map

        out["tags"] = aws_sdk_bedrock_agent.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
