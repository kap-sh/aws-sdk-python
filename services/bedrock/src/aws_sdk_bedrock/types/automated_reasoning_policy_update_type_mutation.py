"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyUpdateTypeMutation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type


class AutomatedReasoningPolicyUpdateTypeMutation(TypedDict):
    type: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type.AutomatedReasoningPolicyDefinitionType"
    """<p>The updated type definition containing the modified name, description, or values for the existing custom type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyUpdateTypeMutation) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type

    out["type"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_definition_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyUpdateTypeMutation:
    out: AutomatedReasoningPolicyUpdateTypeMutation = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type

        out["type"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyUpdateTypeMutation.type required"
        )
    return out
