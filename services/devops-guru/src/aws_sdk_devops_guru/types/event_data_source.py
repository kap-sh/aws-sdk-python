"""Generated from Smithy shape ``com.amazonaws.devopsguru#EventDataSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

EventDataSource: TypeAlias = Literal[
    "AWS_CLOUD_TRAIL",
    "AWS_CODE_DEPLOY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_CLOUD_TRAIL",
        "AWS_CODE_DEPLOY",
    )
)


def serialize_json(value: EventDataSource) -> str:
    return value


def deserialize_json(data: str) -> EventDataSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventDataSource value: {data!r}")
    return cast(EventDataSource, data)
