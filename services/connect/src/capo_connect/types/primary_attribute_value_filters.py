"""Generated from Smithy shape ``com.amazonaws.connect#PrimaryAttributeValueFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.primary_attribute_value_filter

PrimaryAttributeValueFilters: TypeAlias = list[
    "capo_connect.types.primary_attribute_value_filter.PrimaryAttributeValueFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryAttributeValueFilters) -> list:
    import capo_connect.types.primary_attribute_value_filter

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.primary_attribute_value_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PrimaryAttributeValueFilters:
    import capo_connect.types.primary_attribute_value_filter

    out: PrimaryAttributeValueFilters = []
    for item in data:
        out.append(
            capo_connect.types.primary_attribute_value_filter.deserialize_json(item)
        )
    return out
