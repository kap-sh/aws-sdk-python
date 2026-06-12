"""Generated from Smithy shape ``com.amazonaws.codebuild#CommandType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

CommandType: TypeAlias = Literal["SHELL",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SHELL",))


def serialize_aws_json_1_1(value: CommandType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CommandType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CommandType value: {data!r}")
    return cast(CommandType, data)
