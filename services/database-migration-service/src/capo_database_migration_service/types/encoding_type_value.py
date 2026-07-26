"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#EncodingTypeValue``."""

from typing import Literal, TypeAlias, cast

EncodingTypeValue: TypeAlias = Literal[
    "plain",
    "plain-dictionary",
    "rle-dictionary",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncodingTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncodingTypeValue:
    return cast(EncodingTypeValue, data)
