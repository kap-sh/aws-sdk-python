"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAddTypeMutation``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type


class AutomatedReasoningPolicyAddTypeMutation(TypedDict):
    type: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type.AutomatedReasoningPolicyDefinitionType"
    """<p>The type definition that specifies the name, description, and possible values for the new custom type being added to the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAddTypeMutation) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type

    out["type"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_definition_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAddTypeMutation:
    out: AutomatedReasoningPolicyAddTypeMutation = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type

        out["type"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAddTypeMutation.type required"
        )
    return out
