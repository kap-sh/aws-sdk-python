"""Generated from Smithy shape ``com.amazonaws.firehose#SubnetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_firehose.types.non_empty_string_without_whitespace

SubnetIdList: TypeAlias = list[
    "aws_sdk_firehose.types.non_empty_string_without_whitespace.NonEmptyStringWithoutWhitespace"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SubnetIdList:
    return list(data)
