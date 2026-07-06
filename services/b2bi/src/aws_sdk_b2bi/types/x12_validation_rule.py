"""Generated from Smithy shape ``com.amazonaws.b2bi#X12ValidationRule``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_b2bi.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.x12_code_list_validation_rule
    import aws_sdk_b2bi.types.x12_element_length_validation_rule
    import aws_sdk_b2bi.types.x12_element_requirement_validation_rule


class _X12ValidationRule_codeListValidationRule(TypedDict, closed=True):
    codeListValidationRule: (
        "aws_sdk_b2bi.types.x12_code_list_validation_rule.X12CodeListValidationRule"
    )


class _X12ValidationRule_elementLengthValidationRule(TypedDict, closed=True):
    elementLengthValidationRule: "aws_sdk_b2bi.types.x12_element_length_validation_rule.X12ElementLengthValidationRule"


class _X12ValidationRule_elementRequirementValidationRule(TypedDict, closed=True):
    elementRequirementValidationRule: "aws_sdk_b2bi.types.x12_element_requirement_validation_rule.X12ElementRequirementValidationRule"


X12ValidationRule: TypeAlias = (
    _X12ValidationRule_codeListValidationRule
    | _X12ValidationRule_elementLengthValidationRule
    | _X12ValidationRule_elementRequirementValidationRule
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12ValidationRule) -> dict:
    if "codeListValidationRule" in value:
        import aws_sdk_b2bi.types.x12_code_list_validation_rule

        return {
            "codeListValidationRule": aws_sdk_b2bi.types.x12_code_list_validation_rule.serialize_aws_json_1_0(
                value["codeListValidationRule"]
            )
        }
    elif "elementLengthValidationRule" in value:
        import aws_sdk_b2bi.types.x12_element_length_validation_rule

        return {
            "elementLengthValidationRule": aws_sdk_b2bi.types.x12_element_length_validation_rule.serialize_aws_json_1_0(
                value["elementLengthValidationRule"]
            )
        }
    elif "elementRequirementValidationRule" in value:
        import aws_sdk_b2bi.types.x12_element_requirement_validation_rule

        return {
            "elementRequirementValidationRule": aws_sdk_b2bi.types.x12_element_requirement_validation_rule.serialize_aws_json_1_0(
                value["elementRequirementValidationRule"]
            )
        }
    else:
        raise SerializationError("X12ValidationRule: no variant present")


def deserialize_aws_json_1_0(data: dict) -> X12ValidationRule:
    if "codeListValidationRule" in data:
        import aws_sdk_b2bi.types.x12_code_list_validation_rule

        return {
            "codeListValidationRule": aws_sdk_b2bi.types.x12_code_list_validation_rule.deserialize_aws_json_1_0(
                data["codeListValidationRule"]
            )
        }
    elif "elementLengthValidationRule" in data:
        import aws_sdk_b2bi.types.x12_element_length_validation_rule

        return {
            "elementLengthValidationRule": aws_sdk_b2bi.types.x12_element_length_validation_rule.deserialize_aws_json_1_0(
                data["elementLengthValidationRule"]
            )
        }
    elif "elementRequirementValidationRule" in data:
        import aws_sdk_b2bi.types.x12_element_requirement_validation_rule

        return {
            "elementRequirementValidationRule": aws_sdk_b2bi.types.x12_element_requirement_validation_rule.deserialize_aws_json_1_0(
                data["elementRequirementValidationRule"]
            )
        }
    else:
        raise DeserializationError("X12ValidationRule: no recognized variant key")
