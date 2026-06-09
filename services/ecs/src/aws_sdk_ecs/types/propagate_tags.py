"""Generated from Smithy shape ``com.amazonaws.ecs#PropagateTags``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

PropagateTags: TypeAlias = Literal[
    "TASK_DEFINITION",
    "SERVICE",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TASK_DEFINITION",
        "SERVICE",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: PropagateTags) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PropagateTags:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PropagateTags value: {data!r}")
    return cast(PropagateTags, data)
