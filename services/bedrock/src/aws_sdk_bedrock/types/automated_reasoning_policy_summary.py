"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_description
    import aws_sdk_bedrock.types.automated_reasoning_policy_id
    import aws_sdk_bedrock.types.automated_reasoning_policy_name
    import aws_sdk_bedrock.types.automated_reasoning_policy_version
    import aws_sdk_bedrock.types.timestamp


class AutomatedReasoningPolicySummary(TypedDict):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the policy.</p>"""
    name: "aws_sdk_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName"
    """<p>The name of the policy.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_description.AutomatedReasoningPolicyDescription"
    ]
    """<p>The description of the policy.</p>"""
    version: "aws_sdk_bedrock.types.automated_reasoning_policy_version.AutomatedReasoningPolicyVersion"
    """<p>The version of the policy.</p>"""
    policy_id: (
        "aws_sdk_bedrock.types.automated_reasoning_policy_id.AutomatedReasoningPolicyId"
    )
    """<p>The unique identifier of the policy.</p>"""
    created_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the policy was created.</p>"""
    updated_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the policy was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicySummary) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["version"] = value["version"]
    out["policyId"] = value["policy_id"]
    import aws_sdk_bedrock.types.timestamp

    out["createdAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock.types.timestamp

    out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicySummary:
    out: AutomatedReasoningPolicySummary = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicySummary.policy_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AutomatedReasoningPolicySummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("AutomatedReasoningPolicySummary.version required")
    if "policyId" in data:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("AutomatedReasoningPolicySummary.policy_id required")
    if "createdAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["created_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicySummary.created_at required"
        )
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicySummary.updated_at required"
        )
    return out
