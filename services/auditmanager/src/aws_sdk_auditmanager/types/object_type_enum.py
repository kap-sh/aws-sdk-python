"""Generated from Smithy shape ``com.amazonaws.auditmanager#ObjectTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

ObjectTypeEnum: TypeAlias = Literal[
    "ASSESSMENT",
    "CONTROL_SET",
    "CONTROL",
    "DELEGATION",
    "ASSESSMENT_REPORT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSESSMENT",
        "CONTROL_SET",
        "CONTROL",
        "DELEGATION",
        "ASSESSMENT_REPORT",
    )
)


def serialize_json(value: ObjectTypeEnum) -> str:
    return value


def deserialize_json(data: str) -> ObjectTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ObjectTypeEnum value: {data!r}")
    return cast(ObjectTypeEnum, data)
