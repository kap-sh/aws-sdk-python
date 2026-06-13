"""Generated from Smithy shape ``com.amazonaws.applicationsignals#AttributeFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.attribute_filter_value

AttributeFilterValues: TypeAlias = list[
    "aws_sdk_application_signals.types.attribute_filter_value.AttributeFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> AttributeFilterValues:
    return list(data)
