"""Generated from Smithy shape ``com.amazonaws.ecs#EnvironmentFileType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

EnvironmentFileType: TypeAlias = Literal["s3",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("s3",))


def serialize_aws_json_1_1(value: EnvironmentFileType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnvironmentFileType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnvironmentFileType value: {data!r}")
    return cast(EnvironmentFileType, data)
