"""Generated from Smithy shape ``com.amazonaws.frauddetector#fieldValidationMessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.field_validation_message

fieldValidationMessageList: TypeAlias = list[
    "capo_frauddetector.types.field_validation_message.FieldValidationMessage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: fieldValidationMessageList) -> list:
    import capo_frauddetector.types.field_validation_message

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.field_validation_message.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> fieldValidationMessageList:
    import capo_frauddetector.types.field_validation_message

    out: fieldValidationMessageList = []
    for item in data:
        out.append(
            capo_frauddetector.types.field_validation_message.deserialize_aws_json_1_1(
                item
            )
        )
    return out
