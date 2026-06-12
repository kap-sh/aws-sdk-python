"""Generated from Smithy shape ``com.amazonaws.auditmanager#ActionEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE",
        "UPDATE_METADATA",
        "ACTIVE",
        "INACTIVE",
        "DELETE",
        "UNDER_REVIEW",
        "REVIEWED",
        "IMPORT_EVIDENCE",
    )
)


def serialize_json(value: ActionEnum) -> str:
    return value


def deserialize_json(data: str) -> ActionEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionEnum value: {data!r}")
    return cast(ActionEnum, data)
