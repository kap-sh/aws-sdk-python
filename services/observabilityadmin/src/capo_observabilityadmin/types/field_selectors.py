"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#FieldSelectors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.advanced_field_selector

FieldSelectors: TypeAlias = list[
    "capo_observabilityadmin.types.advanced_field_selector.AdvancedFieldSelector"
]


# --- restJson1 ser/de ---
def serialize_json(value: FieldSelectors) -> list:
    import capo_observabilityadmin.types.advanced_field_selector

    out: list = []
    for item in value:
        out.append(
            capo_observabilityadmin.types.advanced_field_selector.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FieldSelectors:
    import capo_observabilityadmin.types.advanced_field_selector

    out: FieldSelectors = []
    for item in data:
        out.append(
            capo_observabilityadmin.types.advanced_field_selector.deserialize_json(item)
        )
    return out
