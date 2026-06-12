"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOf__EndpointTypesElement``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__endpoint_types_element

ListOf__EndpointTypesElement: TypeAlias = list[
    "aws_sdk_pinpoint.types.__endpoint_types_element.__EndpointTypesElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOf__EndpointTypesElement) -> list:
    import aws_sdk_pinpoint.types.__endpoint_types_element

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.__endpoint_types_element.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOf__EndpointTypesElement:
    import aws_sdk_pinpoint.types.__endpoint_types_element

    out: ListOf__EndpointTypesElement = []
    for item in data:
        out.append(
            aws_sdk_pinpoint.types.__endpoint_types_element.deserialize_json(item)
        )
    return out
