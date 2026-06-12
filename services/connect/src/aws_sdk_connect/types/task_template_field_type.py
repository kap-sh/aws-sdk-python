"""Generated from Smithy shape ``com.amazonaws.connect#TaskTemplateFieldType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

TaskTemplateFieldType: TypeAlias = Literal[
    "NAME",
    "DESCRIPTION",
    "SCHEDULED_TIME",
    "QUICK_CONNECT",
    "URL",
    "NUMBER",
    "TEXT",
    "TEXT_AREA",
    "DATE_TIME",
    "BOOLEAN",
    "SINGLE_SELECT",
    "EMAIL",
    "SELF_ASSIGN",
    "EXPIRY_DURATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAME",
        "DESCRIPTION",
        "SCHEDULED_TIME",
        "QUICK_CONNECT",
        "URL",
        "NUMBER",
        "TEXT",
        "TEXT_AREA",
        "DATE_TIME",
        "BOOLEAN",
        "SINGLE_SELECT",
        "EMAIL",
        "SELF_ASSIGN",
        "EXPIRY_DURATION",
    )
)


def serialize_json(value: TaskTemplateFieldType) -> str:
    return value


def deserialize_json(data: str) -> TaskTemplateFieldType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskTemplateFieldType value: {data!r}")
    return cast(TaskTemplateFieldType, data)
