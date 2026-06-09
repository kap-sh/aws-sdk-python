"""Generated from Smithy shape ``com.amazonaws.ecs#TaskField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

TaskField: TypeAlias = Literal["TAGS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TAGS",))


def serialize_aws_json_1_1(value: TaskField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskField value: {data!r}")
    return cast(TaskField, data)
