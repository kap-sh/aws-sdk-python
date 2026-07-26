"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#FieldValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudsearch_domain.types.string

FieldValue: TypeAlias = list["capo_cloudsearch_domain.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: FieldValue) -> list:
    return list(value)


def deserialize_json(data: list) -> FieldValue:
    return list(data)
