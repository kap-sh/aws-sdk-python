"""Generated from Smithy shape ``com.amazonaws.connect#TaskTemplateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

TaskTemplateStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_json(value: TaskTemplateStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskTemplateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskTemplateStatus value: {data!r}")
    return cast(TaskTemplateStatus, data)
