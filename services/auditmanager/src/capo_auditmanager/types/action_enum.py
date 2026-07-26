"""Generated from Smithy shape ``com.amazonaws.auditmanager#ActionEnum``."""

from typing import Literal, TypeAlias, cast

ActionEnum: TypeAlias = Literal[
    "CREATE",
    "UPDATE_METADATA",
    "ACTIVE",
    "INACTIVE",
    "DELETE",
    "UNDER_REVIEW",
    "REVIEWED",
    "IMPORT_EVIDENCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionEnum) -> str:
    return value


def deserialize_json(data: str) -> ActionEnum:
    return cast(ActionEnum, data)
