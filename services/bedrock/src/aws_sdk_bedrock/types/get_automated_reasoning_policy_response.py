"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_description
    import aws_sdk_bedrock.types.automated_reasoning_policy_hash
    import aws_sdk_bedrock.types.automated_reasoning_policy_id
    import aws_sdk_bedrock.types.automated_reasoning_policy_name
    import aws_sdk_bedrock.types.automated_reasoning_policy_version
    import aws_sdk_bedrock.types.kms_key_arn
    import aws_sdk_bedrock.types.timestamp


class GetAutomatedReasoningPolicyResponse(TypedDict):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the policy.</p>"""
    name: "aws_sdk_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName"
    """<p>The name of the policy.</p>"""
    version: "aws_sdk_bedrock.types.automated_reasoning_policy_version.AutomatedReasoningPolicyVersion"
    """<p>The version of the policy.</p>"""
    policy_id: (
        "aws_sdk_bedrock.types.automated_reasoning_policy_id.AutomatedReasoningPolicyId"
    )
    """<p>The unique identifier of the policy.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_description.AutomatedReasoningPolicyDescription"
    ]
    """<p>The description of the policy.</p>"""
    definition_hash: "aws_sdk_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash"
    """<p>The hash of the policy definition used as a concurrency token.</p>"""
    kms_key_arn: NotRequired["aws_sdk_bedrock.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the automated reasoning policy and its associated artifacts. If a KMS key is not provided during the initial CreateAutomatedReasoningPolicyRequest, the kmsKeyArn won't be included in the GetAutomatedReasoningPolicyResponse. </p>"""
    created_at: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>The timestamp when the policy was created.</p>"""
    updated_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the policy was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedReasoningPolicyResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["name"] = value["name"]
    out["version"] = value["version"]
    out["policyId"] = value["policy_id"]
    if "description" in value:
        out["description"] = value["description"]
    out["definitionHash"] = value["definition_hash"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "created_at" in value:
        import aws_sdk_bedrock.types.timestamp

        out["createdAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["created_at"]
        )
    import aws_sdk_bedrock.types.timestamp

    out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> GetAutomatedReasoningPolicyResponse:
    out: GetAutomatedReasoningPolicyResponse = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyResponse.policy_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetAutomatedReasoningPolicyResponse.name required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyResponse.version required"
        )
    if "policyId" in data:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyResponse.policy_id required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "definitionHash" in data:
        out["definition_hash"] = data["definitionHash"]
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyResponse.definition_hash required"
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "createdAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["created_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyResponse.updated_at required"
        )
    return out
