"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Validation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.number_validation
    import aws_sdk_bedrock_agentcore_control.types.string_list_validation
    import aws_sdk_bedrock_agentcore_control.types.string_validation


class _Validation_stringValidation(TypedDict, closed=True):
    stringValidation: (
        "aws_sdk_bedrock_agentcore_control.types.string_validation.StringValidation"
    )


class _Validation_stringListValidation(TypedDict, closed=True):
    stringListValidation: "aws_sdk_bedrock_agentcore_control.types.string_list_validation.StringListValidation"


class _Validation_numberValidation(TypedDict, closed=True):
    numberValidation: (
        "aws_sdk_bedrock_agentcore_control.types.number_validation.NumberValidation"
    )


Validation: TypeAlias = (
    _Validation_stringValidation
    | _Validation_stringListValidation
    | _Validation_numberValidation
)


# --- restJson1 ser/de ---
def serialize_json(value: Validation) -> dict:
    if "stringValidation" in value:
        import aws_sdk_bedrock_agentcore_control.types.string_validation

        return {
            "stringValidation": aws_sdk_bedrock_agentcore_control.types.string_validation.serialize_json(
                value["stringValidation"]
            )
        }
    elif "stringListValidation" in value:
        import aws_sdk_bedrock_agentcore_control.types.string_list_validation

        return {
            "stringListValidation": aws_sdk_bedrock_agentcore_control.types.string_list_validation.serialize_json(
                value["stringListValidation"]
            )
        }
    elif "numberValidation" in value:
        import aws_sdk_bedrock_agentcore_control.types.number_validation

        return {
            "numberValidation": aws_sdk_bedrock_agentcore_control.types.number_validation.serialize_json(
                value["numberValidation"]
            )
        }
    else:
        raise SerializationError("Validation: no variant present")


def deserialize_json(data: dict) -> Validation:
    if "stringValidation" in data:
        import aws_sdk_bedrock_agentcore_control.types.string_validation

        return {
            "stringValidation": aws_sdk_bedrock_agentcore_control.types.string_validation.deserialize_json(
                data["stringValidation"]
            )
        }
    elif "stringListValidation" in data:
        import aws_sdk_bedrock_agentcore_control.types.string_list_validation

        return {
            "stringListValidation": aws_sdk_bedrock_agentcore_control.types.string_list_validation.deserialize_json(
                data["stringListValidation"]
            )
        }
    elif "numberValidation" in data:
        import aws_sdk_bedrock_agentcore_control.types.number_validation

        return {
            "numberValidation": aws_sdk_bedrock_agentcore_control.types.number_validation.deserialize_json(
                data["numberValidation"]
            )
        }
    else:
        raise DeserializationError("Validation: no recognized variant key")
