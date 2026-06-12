"""Generated from Smithy shape ``com.amazonaws.firehose#ListOfNonEmptyStrings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_firehose.types.non_empty_string

ListOfNonEmptyStrings: TypeAlias = list[
    "aws_sdk_firehose.types.non_empty_string.NonEmptyString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfNonEmptyStrings) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ListOfNonEmptyStrings:
    return list(data)
