"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateAutomatedReasoningPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_hash
    import aws_sdk_bedrock.types.automated_reasoning_policy_name
    import aws_sdk_bedrock.types.timestamp


class UpdateAutomatedReasoningPolicyResponse(TypedDict, closed=True):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the updated policy.</p>"""
    name: "aws_sdk_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName"
    """<p>The updated name of the policy.</p>"""
    definition_hash: "aws_sdk_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash"
    """<p>The hash of the updated policy definition.</p>"""
    updated_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the policy was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAutomatedReasoningPolicyResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["name"] = value["name"]
    out["definitionHash"] = value["definition_hash"]
    import aws_sdk_bedrock.types.timestamp

    out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> UpdateAutomatedReasoningPolicyResponse:
    out: UpdateAutomatedReasoningPolicyResponse = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyResponse.policy_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyResponse.name required"
        )
    if "definitionHash" in data:
        out["definition_hash"] = data["definitionHash"]
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyResponse.definition_hash required"
        )
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyResponse.updated_at required"
        )
    return out
