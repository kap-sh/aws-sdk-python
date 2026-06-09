"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinitionField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

TaskDefinitionField: TypeAlias = Literal["TAGS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TAGS",))


def serialize_aws_json_1_1(value: TaskDefinitionField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskDefinitionField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskDefinitionField value: {data!r}")
    return cast(TaskDefinitionField, data)
