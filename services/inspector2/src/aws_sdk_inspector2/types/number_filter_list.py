"""Generated from Smithy shape ``com.amazonaws.inspector2#NumberFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.number_filter

NumberFilterList: TypeAlias = list[
    "aws_sdk_inspector2.types.number_filter.NumberFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: NumberFilterList) -> list:
    import aws_sdk_inspector2.types.number_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.number_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> NumberFilterList:
    import aws_sdk_inspector2.types.number_filter

    out: NumberFilterList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.number_filter.deserialize_json(item))
    return out
