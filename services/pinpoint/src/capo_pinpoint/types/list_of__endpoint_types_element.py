"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOf__EndpointTypesElement``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.__endpoint_types_element

ListOf__EndpointTypesElement: TypeAlias = list[
    "capo_pinpoint.types.__endpoint_types_element.__EndpointTypesElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOf__EndpointTypesElement) -> list:
    import capo_pinpoint.types.__endpoint_types_element

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.__endpoint_types_element.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOf__EndpointTypesElement:
    import capo_pinpoint.types.__endpoint_types_element

    out: ListOf__EndpointTypesElement = []
    for item in data:
        out.append(capo_pinpoint.types.__endpoint_types_element.deserialize_json(item))
    return out
