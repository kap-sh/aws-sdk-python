"""Generated from Smithy shape ``com.amazonaws.codecommit#RelativeFileVersionEnum``."""

from typing import Literal, TypeAlias, cast

RelativeFileVersionEnum: TypeAlias = Literal[
    "BEFORE",
    "AFTER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelativeFileVersionEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RelativeFileVersionEnum:
    return cast(RelativeFileVersionEnum, data)
