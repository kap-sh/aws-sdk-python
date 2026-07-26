"""Generated from Smithy shape ``com.amazonaws.codecommit#FileModeTypeEnum``."""

from typing import Literal, TypeAlias, cast

FileModeTypeEnum: TypeAlias = Literal[
    "EXECUTABLE",
    "NORMAL",
    "SYMLINK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileModeTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileModeTypeEnum:
    return cast(FileModeTypeEnum, data)
