"""Generated from Smithy shape ``com.amazonaws.applicationsignals#AttributeFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.attribute_filter

AttributeFilters: TypeAlias = list[
    "capo_application_signals.types.attribute_filter.AttributeFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeFilters) -> list:
    import capo_application_signals.types.attribute_filter

    out: list = []
    for item in value:
        out.append(capo_application_signals.types.attribute_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttributeFilters:
    import capo_application_signals.types.attribute_filter

    out: AttributeFilters = []
    for item in data:
        out.append(
            capo_application_signals.types.attribute_filter.deserialize_json(item)
        )
    return out
