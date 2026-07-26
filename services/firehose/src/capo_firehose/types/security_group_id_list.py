"""Generated from Smithy shape ``com.amazonaws.firehose#SecurityGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_firehose.types.non_empty_string_without_whitespace

SecurityGroupIdList: TypeAlias = list[
    "capo_firehose.types.non_empty_string_without_whitespace.NonEmptyStringWithoutWhitespace"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SecurityGroupIdList:
    return list(data)
