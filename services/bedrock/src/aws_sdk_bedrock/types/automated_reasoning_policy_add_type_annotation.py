"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAddTypeAnnotation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_description
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_list


class AutomatedReasoningPolicyAddTypeAnnotation(TypedDict, closed=True):
    name: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name.AutomatedReasoningPolicyDefinitionTypeName"
    """<p>The name of the new custom type. This name will be used to reference the type in variable definitions and rules.</p>"""
    description: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_description.AutomatedReasoningPolicyDefinitionTypeDescription"
    """<p>A description of what the custom type represents and how it should be used in the policy.</p>"""
    values: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_list.AutomatedReasoningPolicyDefinitionTypeValueList"
    """<p>The list of possible values that variables of this type can take, each with its own description and identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAddTypeAnnotation) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["description"] = value["description"]
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_list

    out["values"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_list.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAddTypeAnnotation:
    out: AutomatedReasoningPolicyAddTypeAnnotation = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAddTypeAnnotation.name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAddTypeAnnotation.description required"
        )
    if "values" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_list

        out["values"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_list.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAddTypeAnnotation.values required"
        )
    return out
