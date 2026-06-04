"""Generated from Smithy shape ``com.amazonaws.ecs#TaskSetField``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

TaskSetField: TypeAlias = Literal["TAGS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TAGS",))


def serialize_aws_json_1_1(value: TaskSetField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskSetField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskSetField value: {data!r}")
    return cast(TaskSetField, data)
