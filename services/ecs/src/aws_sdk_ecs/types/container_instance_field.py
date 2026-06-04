"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerInstanceField``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

ContainerInstanceField: TypeAlias = Literal[
    "TAGS",
    "CONTAINER_INSTANCE_HEALTH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TAGS",
        "CONTAINER_INSTANCE_HEALTH",
    )
)


def serialize_aws_json_1_1(value: ContainerInstanceField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerInstanceField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerInstanceField value: {data!r}")
    return cast(ContainerInstanceField, data)
