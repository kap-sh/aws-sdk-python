"""Generated from Smithy shape ``com.amazonaws.connecthealth#ManagedNoteTemplate``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connecthealth.errors import DeserializationError

ManagedNoteTemplate: TypeAlias = Literal[
    "HISTORY_AND_PHYSICAL",
    "GIRPP",
    "DAP",
    "SIRP",
    "BIRP",
    "BEHAVIORAL_SOAP",
    "PHYSICAL_SOAP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HISTORY_AND_PHYSICAL",
        "GIRPP",
        "DAP",
        "SIRP",
        "BIRP",
        "BEHAVIORAL_SOAP",
        "PHYSICAL_SOAP",
    )
)


def serialize_json(value: ManagedNoteTemplate) -> str:
    return value


def deserialize_json(data: str) -> ManagedNoteTemplate:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ManagedNoteTemplate value: {data!r}")
    return cast(ManagedNoteTemplate, data)
