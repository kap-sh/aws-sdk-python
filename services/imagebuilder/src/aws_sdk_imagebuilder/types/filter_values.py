"""Generated from Smithy shape ``com.amazonaws.imagebuilder#FilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.filter_value

FilterValues: TypeAlias = list["aws_sdk_imagebuilder.types.filter_value.FilterValue"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterValues:
    return list(data)
