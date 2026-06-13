"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDeleteVariableMutation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name


class AutomatedReasoningPolicyDeleteVariableMutation(TypedDict):
    name: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name.AutomatedReasoningPolicyDefinitionVariableName"
    """<p>The name of the variable to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDeleteVariableMutation) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDeleteVariableMutation:
    out: AutomatedReasoningPolicyDeleteVariableMutation = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDeleteVariableMutation.name required"
        )
    return out
