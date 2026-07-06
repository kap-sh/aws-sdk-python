"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyUpdateTypeAnnotation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_description
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name
    import aws_sdk_bedrock.types.automated_reasoning_policy_type_value_annotation_list


class AutomatedReasoningPolicyUpdateTypeAnnotation(TypedDict, closed=True):
    name: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name.AutomatedReasoningPolicyDefinitionTypeName"
    """<p>The current name of the custom type to update.</p>"""
    new_name: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_name.AutomatedReasoningPolicyDefinitionTypeName"
    ]
    """<p>The new name for the custom type, if you want to rename it. If not provided, the name remains unchanged.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_description.AutomatedReasoningPolicyDefinitionTypeDescription"
    ]
    """<p>The new description for the custom type, replacing the previous description.</p>"""
    values: "aws_sdk_bedrock.types.automated_reasoning_policy_type_value_annotation_list.AutomatedReasoningPolicyTypeValueAnnotationList"
    """<p>The updated list of values for the custom type, which can include additions, modifications, or removals.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyUpdateTypeAnnotation) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "new_name" in value:
        out["newName"] = value["new_name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock.types.automated_reasoning_policy_type_value_annotation_list

    out["values"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_type_value_annotation_list.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyUpdateTypeAnnotation:
    out: AutomatedReasoningPolicyUpdateTypeAnnotation = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyUpdateTypeAnnotation.name required"
        )
    if "newName" in data:
        out["new_name"] = data["newName"]
    if "description" in data:
        out["description"] = data["description"]
    if "values" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_type_value_annotation_list

        out["values"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_type_value_annotation_list.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyUpdateTypeAnnotation.values required"
        )
    return out
