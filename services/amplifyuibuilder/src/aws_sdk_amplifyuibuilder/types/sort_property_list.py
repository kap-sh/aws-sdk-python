"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#SortPropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.sort_property

SortPropertyList: TypeAlias = list[
    "aws_sdk_amplifyuibuilder.types.sort_property.SortProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: SortPropertyList) -> list:
    import aws_sdk_amplifyuibuilder.types.sort_property

    out: list = []
    for item in value:
        out.append(aws_sdk_amplifyuibuilder.types.sort_property.serialize_json(item))
    return out


def deserialize_json(data: list) -> SortPropertyList:
    import aws_sdk_amplifyuibuilder.types.sort_property

    out: SortPropertyList = []
    for item in data:
        out.append(aws_sdk_amplifyuibuilder.types.sort_property.deserialize_json(item))
    return out
