"""Generated from Smithy shape ``com.amazonaws.auditmanager#ObjectTypeEnum``."""

from typing import Literal, TypeAlias, cast

ObjectTypeEnum: TypeAlias = Literal[
    "ASSESSMENT",
    "CONTROL_SET",
    "CONTROL",
    "DELEGATION",
    "ASSESSMENT_REPORT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ObjectTypeEnum) -> str:
    return value


def deserialize_json(data: str) -> ObjectTypeEnum:
    return cast(ObjectTypeEnum, data)
