"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionTypeValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_description
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_name


class AutomatedReasoningPolicyDefinitionTypeValue(TypedDict):
    value: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_name.AutomatedReasoningPolicyDefinitionTypeValueName"
    """<p>The actual value or identifier for this type value.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_definition_type_value_description.AutomatedReasoningPolicyDefinitionTypeValueDescription"
    ]
    """<p>A human-readable description explaining what this type value represents and when it should be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionTypeValue) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDefinitionTypeValue:
    out: AutomatedReasoningPolicyDefinitionTypeValue = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionTypeValue.value required"
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
