"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#RedactedFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.field_to_match

RedactedFields: TypeAlias = list[
    "capo_observabilityadmin.types.field_to_match.FieldToMatch"
]


# --- restJson1 ser/de ---
def serialize_json(value: RedactedFields) -> list:
    import capo_observabilityadmin.types.field_to_match

    out: list = []
    for item in value:
        out.append(capo_observabilityadmin.types.field_to_match.serialize_json(item))
    return out


def deserialize_json(data: list) -> RedactedFields:
    import capo_observabilityadmin.types.field_to_match

    out: RedactedFields = []
    for item in data:
        out.append(capo_observabilityadmin.types.field_to_match.deserialize_json(item))
    return out
