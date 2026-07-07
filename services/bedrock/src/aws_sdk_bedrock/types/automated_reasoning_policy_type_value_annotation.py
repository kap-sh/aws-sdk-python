"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyTypeValueAnnotation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_add_type_value
    import aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_value
    import aws_sdk_bedrock.types.automated_reasoning_policy_update_type_value


class _AutomatedReasoningPolicyTypeValueAnnotation_addTypeValue(TypedDict, closed=True):
    addTypeValue: "aws_sdk_bedrock.types.automated_reasoning_policy_add_type_value.AutomatedReasoningPolicyAddTypeValue"


class _AutomatedReasoningPolicyTypeValueAnnotation_updateTypeValue(
    TypedDict, closed=True
):
    updateTypeValue: "aws_sdk_bedrock.types.automated_reasoning_policy_update_type_value.AutomatedReasoningPolicyUpdateTypeValue"


class _AutomatedReasoningPolicyTypeValueAnnotation_deleteTypeValue(
    TypedDict, closed=True
):
    deleteTypeValue: "aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_value.AutomatedReasoningPolicyDeleteTypeValue"


AutomatedReasoningPolicyTypeValueAnnotation: TypeAlias = (
    _AutomatedReasoningPolicyTypeValueAnnotation_addTypeValue
    | _AutomatedReasoningPolicyTypeValueAnnotation_updateTypeValue
    | _AutomatedReasoningPolicyTypeValueAnnotation_deleteTypeValue
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyTypeValueAnnotation) -> dict:
    if "addTypeValue" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_add_type_value

        return {
            "addTypeValue": aws_sdk_bedrock.types.automated_reasoning_policy_add_type_value.serialize_json(
                value["addTypeValue"]
            )
        }
    elif "updateTypeValue" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_type_value

        return {
            "updateTypeValue": aws_sdk_bedrock.types.automated_reasoning_policy_update_type_value.serialize_json(
                value["updateTypeValue"]
            )
        }
    elif "deleteTypeValue" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_value

        return {
            "deleteTypeValue": aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_value.serialize_json(
                value["deleteTypeValue"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedReasoningPolicyTypeValueAnnotation: no variant present"
        )


def deserialize_json(data: dict) -> AutomatedReasoningPolicyTypeValueAnnotation:
    if "addTypeValue" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_add_type_value

        return {
            "addTypeValue": aws_sdk_bedrock.types.automated_reasoning_policy_add_type_value.deserialize_json(
                data["addTypeValue"]
            )
        }
    elif "updateTypeValue" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_update_type_value

        return {
            "updateTypeValue": aws_sdk_bedrock.types.automated_reasoning_policy_update_type_value.deserialize_json(
                data["updateTypeValue"]
            )
        }
    elif "deleteTypeValue" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_value

        return {
            "deleteTypeValue": aws_sdk_bedrock.types.automated_reasoning_policy_delete_type_value.deserialize_json(
                data["deleteTypeValue"]
            )
        }
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyTypeValueAnnotation: no recognized variant key"
        )
