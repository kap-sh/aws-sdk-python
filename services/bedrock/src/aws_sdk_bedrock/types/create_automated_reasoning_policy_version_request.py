"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateAutomatedReasoningPolicyVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_hash
    import aws_sdk_bedrock.types.idempotency_token
    import aws_sdk_bedrock.types.tag_list


class CreateAutomatedReasoningPolicyVersionRequest(TypedDict):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to create a version.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>"""
    last_updated_definition_hash: "aws_sdk_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash"
    """<p>The hash of the current policy definition used as a concurrency token to ensure the policy hasn't been modified since you last retrieved it.</p>"""
    tags: NotRequired["aws_sdk_bedrock.types.tag_list.TagList"]
    """<p>A list of tags to associate with the policy version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAutomatedReasoningPolicyVersionRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["lastUpdatedDefinitionHash"] = value["last_updated_definition_hash"]
    if "tags" in value:
        import aws_sdk_bedrock.types.tag_list

        out["tags"] = aws_sdk_bedrock.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAutomatedReasoningPolicyVersionRequest:
    out: CreateAutomatedReasoningPolicyVersionRequest = {}  # type: ignore[typeddict-item]
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "lastUpdatedDefinitionHash" in data:
        out["last_updated_definition_hash"] = data["lastUpdatedDefinitionHash"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyVersionRequest.last_updated_definition_hash required"
        )
    if "tags" in data:
        import aws_sdk_bedrock.types.tag_list

        out["tags"] = aws_sdk_bedrock.types.tag_list.deserialize_json(data["tags"])
    return out
