"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateAutomatedReasoningPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_description
    import aws_sdk_bedrock.types.automated_reasoning_policy_hash
    import aws_sdk_bedrock.types.automated_reasoning_policy_name
    import aws_sdk_bedrock.types.automated_reasoning_policy_version
    import aws_sdk_bedrock.types.timestamp


class CreateAutomatedReasoningPolicyResponse(TypedDict, closed=True):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy that you created.</p>"""
    version: "aws_sdk_bedrock.types.automated_reasoning_policy_version.AutomatedReasoningPolicyVersion"
    """<p>The version number of the newly created Automated Reasoning policy. The initial version is always DRAFT.</p>"""
    name: "aws_sdk_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName"
    """<p>The name of the Automated Reasoning policy.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_description.AutomatedReasoningPolicyDescription"
    ]
    """<p>The description of the Automated Reasoning policy.</p>"""
    definition_hash: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash"
    ]
    """<p>The hash of the policy definition. This is used as a concurrency token for creating policy versions that you can use in your application.</p>"""
    created_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the policy was created.</p>"""
    updated_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the policy was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAutomatedReasoningPolicyResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["version"] = value["version"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "definition_hash" in value:
        out["definitionHash"] = value["definition_hash"]
    import aws_sdk_bedrock.types.timestamp

    out["createdAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock.types.timestamp

    out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> CreateAutomatedReasoningPolicyResponse:
    out: CreateAutomatedReasoningPolicyResponse = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyResponse.policy_arn required"
        )
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyResponse.version required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyResponse.name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "definitionHash" in data:
        out["definition_hash"] = data["definitionHash"]
    if "createdAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["created_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyResponse.created_at required"
        )
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyResponse.updated_at required"
        )
    return out
