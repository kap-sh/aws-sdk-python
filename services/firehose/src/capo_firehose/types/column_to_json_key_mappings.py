"""Generated from Smithy shape ``com.amazonaws.firehose#ColumnToJsonKeyMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_firehose.types.non_empty_string
    import capo_firehose.types.non_empty_string_without_whitespace

ColumnToJsonKeyMappings: TypeAlias = dict[
    "capo_firehose.types.non_empty_string_without_whitespace.NonEmptyStringWithoutWhitespace",
    "capo_firehose.types.non_empty_string.NonEmptyString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ColumnToJsonKeyMappings) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ColumnToJsonKeyMappings:
    out: ColumnToJsonKeyMappings = {}
    for key, value in data.items():
        out[key] = value
    return out
