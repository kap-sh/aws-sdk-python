"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.property_filter

PropertyFilters: TypeAlias = list[
    "aws_sdk_iottwinmaker.types.property_filter.PropertyFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: PropertyFilters) -> list:
    import aws_sdk_iottwinmaker.types.property_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_iottwinmaker.types.property_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> PropertyFilters:
    import aws_sdk_iottwinmaker.types.property_filter

    out: PropertyFilters = []
    for item in data:
        out.append(aws_sdk_iottwinmaker.types.property_filter.deserialize_json(item))
    return out
