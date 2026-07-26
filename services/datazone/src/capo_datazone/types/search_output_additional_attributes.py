"""Generated from Smithy shape ``com.amazonaws.datazone#SearchOutputAdditionalAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.search_output_additional_attribute

SearchOutputAdditionalAttributes: TypeAlias = list[
    "capo_datazone.types.search_output_additional_attribute.SearchOutputAdditionalAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchOutputAdditionalAttributes) -> list:
    import capo_datazone.types.search_output_additional_attribute

    out: list = []
    for item in value:
        out.append(
            capo_datazone.types.search_output_additional_attribute.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchOutputAdditionalAttributes:
    import capo_datazone.types.search_output_additional_attribute

    out: SearchOutputAdditionalAttributes = []
    for item in data:
        out.append(
            capo_datazone.types.search_output_additional_attribute.deserialize_json(
                item
            )
        )
    return out
