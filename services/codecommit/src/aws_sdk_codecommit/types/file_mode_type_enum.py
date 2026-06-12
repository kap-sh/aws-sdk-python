"""Generated from Smithy shape ``com.amazonaws.codecommit#FileModeTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codecommit.errors import DeserializationError

FileModeTypeEnum: TypeAlias = Literal[
    "EXECUTABLE",
    "NORMAL",
    "SYMLINK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXECUTABLE",
        "NORMAL",
        "SYMLINK",
    )
)


def serialize_aws_json_1_1(value: FileModeTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileModeTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileModeTypeEnum value: {data!r}")
    return cast(FileModeTypeEnum, data)
