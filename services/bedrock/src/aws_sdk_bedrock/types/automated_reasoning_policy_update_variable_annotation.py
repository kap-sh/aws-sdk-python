"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyUpdateVariableAnnotation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_description
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name


class AutomatedReasoningPolicyUpdateVariableAnnotation(TypedDict):
    name: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name.AutomatedReasoningPolicyDefinitionVariableName"
    """<p>The current name of the variable to update.</p>"""
    new_name: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_name.AutomatedReasoningPolicyDefinitionVariableName"
    ]
    """<p>The new name for the variable, if you want to rename it. If not provided, the name remains unchanged.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_definition_variable_description.AutomatedReasoningPolicyDefinitionVariableDescription"
    ]
    """<p>The new description for the variable, replacing the previous description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyUpdateVariableAnnotation) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "new_name" in value:
        out["newName"] = value["new_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyUpdateVariableAnnotation:
    out: AutomatedReasoningPolicyUpdateVariableAnnotation = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyUpdateVariableAnnotation.name required"
        )
    if "newName" in data:
        out["new_name"] = data["newName"]
    if "description" in data:
        out["description"] = data["description"]
    return out
