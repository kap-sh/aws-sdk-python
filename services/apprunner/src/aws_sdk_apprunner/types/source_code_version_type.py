"""Generated from Smithy shape ``com.amazonaws.apprunner#SourceCodeVersionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apprunner.errors import DeserializationError

SourceCodeVersionType: TypeAlias = Literal["BRANCH",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("BRANCH",))


def serialize_aws_json_1_0(value: SourceCodeVersionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SourceCodeVersionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceCodeVersionType value: {data!r}")
    return cast(SourceCodeVersionType, data)
