"""Generated from Smithy shape ``com.amazonaws.codecommit#ConflictDetailLevelTypeEnum``."""

from typing import Literal, TypeAlias, cast

ConflictDetailLevelTypeEnum: TypeAlias = Literal[
    "FILE_LEVEL",
    "LINE_LEVEL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConflictDetailLevelTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConflictDetailLevelTypeEnum:
    return cast(ConflictDetailLevelTypeEnum, data)
