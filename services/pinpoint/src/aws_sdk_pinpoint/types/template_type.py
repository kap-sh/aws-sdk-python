"""Generated from Smithy shape ``com.amazonaws.pinpoint#TemplateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

TemplateType: TypeAlias = Literal[
    "EMAIL",
    "SMS",
    "VOICE",
    "PUSH",
    "INAPP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMAIL",
        "SMS",
        "VOICE",
        "PUSH",
        "INAPP",
    )
)


def serialize_json(value: TemplateType) -> str:
    return value


def deserialize_json(data: str) -> TemplateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TemplateType value: {data!r}")
    return cast(TemplateType, data)
