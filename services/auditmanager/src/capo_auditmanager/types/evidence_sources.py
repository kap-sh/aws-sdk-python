"""Generated from Smithy shape ``com.amazonaws.auditmanager#EvidenceSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.non_empty_string

EvidenceSources: TypeAlias = list[
    "capo_auditmanager.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvidenceSources) -> list:
    return list(value)


def deserialize_json(data: list) -> EvidenceSources:
    return list(data)
