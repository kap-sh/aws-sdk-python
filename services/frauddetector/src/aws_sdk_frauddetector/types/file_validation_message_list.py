"""Generated from Smithy shape ``com.amazonaws.frauddetector#fileValidationMessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.file_validation_message

fileValidationMessageList: TypeAlias = list[
    "aws_sdk_frauddetector.types.file_validation_message.FileValidationMessage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: fileValidationMessageList) -> list:
    import aws_sdk_frauddetector.types.file_validation_message

    out: list = []
    for item in value:
        out.append(
            aws_sdk_frauddetector.types.file_validation_message.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> fileValidationMessageList:
    import aws_sdk_frauddetector.types.file_validation_message

    out: fileValidationMessageList = []
    for item in data:
        out.append(
            aws_sdk_frauddetector.types.file_validation_message.deserialize_aws_json_1_1(
                item
            )
        )
    return out
