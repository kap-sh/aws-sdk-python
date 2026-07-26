"""Generated from Smithy shape ``com.amazonaws.auditmanager#ValidationErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.non_empty_string

ValidationErrors: TypeAlias = list[
    "capo_auditmanager.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationErrors) -> list:
    return list(value)


def deserialize_json(data: list) -> ValidationErrors:
    return list(data)
