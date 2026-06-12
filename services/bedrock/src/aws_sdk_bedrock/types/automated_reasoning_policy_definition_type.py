"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionType``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_description
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_list


class AutomatedReasoningPolicyDefinitionType(TypedDict):
    name: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name.AutomatedReasoningPolicyDefinitionTypeName"
    """<p>The name of the custom type.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_description.AutomatedReasoningPolicyDefinitionTypeDescription"
    ]
    """<p>The description of what the custom type represents.</p>"""
    values: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_list.AutomatedReasoningPolicyDefinitionTypeValueList"
    """<p>The possible values for this enum-based type, each with its own description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionType) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_list

    out["values"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_list.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDefinitionType:
    out: AutomatedReasoningPolicyDefinitionType = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionType.name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "values" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_list

        out["values"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_list.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionType.values required"
        )
    return out
