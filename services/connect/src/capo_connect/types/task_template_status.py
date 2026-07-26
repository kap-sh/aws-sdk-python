"""Generated from Smithy shape ``com.amazonaws.connect#TaskTemplateStatus``."""

from typing import Literal, TypeAlias, cast

TaskTemplateStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskTemplateStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskTemplateStatus:
    return cast(TaskTemplateStatus, data)
