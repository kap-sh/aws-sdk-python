"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateAutomatedReasoningPolicyVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_description
    import aws_sdk_bedrock.types.automated_reasoning_policy_hash
    import aws_sdk_bedrock.types.automated_reasoning_policy_name
    import aws_sdk_bedrock.types.automated_reasoning_policy_version
    import aws_sdk_bedrock.types.timestamp


class CreateAutomatedReasoningPolicyVersionResponse(TypedDict):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The versioned Amazon Resource Name (ARN) of the policy version.</p>"""
    version: "aws_sdk_bedrock.types.automated_reasoning_policy_version.AutomatedReasoningPolicyVersion"
    """<p>The version number of the policy version.</p>"""
    name: "aws_sdk_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName"
    """<p>The name of the policy version.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_description.AutomatedReasoningPolicyDescription"
    ]
    """<p>The description of the policy version.</p>"""
    definition_hash: "aws_sdk_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash"
    """<p>The hash of the policy definition for this version.</p>"""
    created_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the policy version was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAutomatedReasoningPolicyVersionResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["version"] = value["version"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["definitionHash"] = value["definition_hash"]
    import aws_sdk_bedrock.types.timestamp

    out["createdAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> CreateAutomatedReasoningPolicyVersionResponse:
    out: CreateAutomatedReasoningPolicyVersionResponse = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyVersionResponse.policy_arn required"
        )
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyVersionResponse.version required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyVersionResponse.name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "definitionHash" in data:
        out["definition_hash"] = data["definitionHash"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyVersionResponse.definition_hash required"
        )
    if "createdAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["created_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyVersionResponse.created_at required"
        )
    return out
