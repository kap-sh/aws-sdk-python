"""Generated from Smithy shape ``com.amazonaws.ram#AssociatedSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ram.types.associated_source

AssociatedSourceList: TypeAlias = list[
    "aws_sdk_ram.types.associated_source.AssociatedSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedSourceList) -> list:
    import aws_sdk_ram.types.associated_source

    out: list = []
    for item in value:
        out.append(aws_sdk_ram.types.associated_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedSourceList:
    import aws_sdk_ram.types.associated_source

    out: AssociatedSourceList = []
    for item in data:
        out.append(aws_sdk_ram.types.associated_source.deserialize_json(item))
    return out
