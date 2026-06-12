"""Generated from Smithy shape ``com.amazonaws.firehose#ListOfNonEmptyStringsWithoutWhitespace``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_firehose.types.non_empty_string_without_whitespace

ListOfNonEmptyStringsWithoutWhitespace: TypeAlias = list[
    "aws_sdk_firehose.types.non_empty_string_without_whitespace.NonEmptyStringWithoutWhitespace"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfNonEmptyStringsWithoutWhitespace) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ListOfNonEmptyStringsWithoutWhitespace:
    return list(data)
