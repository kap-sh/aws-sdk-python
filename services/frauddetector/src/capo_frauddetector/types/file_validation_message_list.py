"""Generated from Smithy shape ``com.amazonaws.frauddetector#fileValidationMessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.file_validation_message

fileValidationMessageList: TypeAlias = list[
    "capo_frauddetector.types.file_validation_message.FileValidationMessage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: fileValidationMessageList) -> list:
    import capo_frauddetector.types.file_validation_message

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.file_validation_message.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> fileValidationMessageList:
    import capo_frauddetector.types.file_validation_message

    out: fileValidationMessageList = []
    for item in data:
        out.append(
            capo_frauddetector.types.file_validation_message.deserialize_aws_json_1_1(
                item
            )
        )
    return out
