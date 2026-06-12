"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttributeFilters``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.attribute_filter

AttributeFilters: TypeAlias = list["aws_sdk_qbusiness.types.attribute_filter.AttributeFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeFilters) -> list:
    import aws_sdk_qbusiness.types.attribute_filter
    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.attribute_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttributeFilters:
    import aws_sdk_qbusiness.types.attribute_filter
    out: AttributeFilters = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.attribute_filter.deserialize_json(item))
    return out