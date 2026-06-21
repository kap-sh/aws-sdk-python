"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MessageFormatValue``."""

from typing import Literal, TypeAlias, cast

MessageFormatValue: TypeAlias = Literal[
    "json",
    "json-unformatted",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MessageFormatValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MessageFormatValue:
    return cast(MessageFormatValue, data)
