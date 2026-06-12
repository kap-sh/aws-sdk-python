"""Generated from Smithy shape ``com.amazonaws.datapipeline#validationMessages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.validation_message

validationMessages: TypeAlias = list[
    "aws_sdk_data_pipeline.types.validation_message.validationMessage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: validationMessages) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> validationMessages:
    return list(data)
