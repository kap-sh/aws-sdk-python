"""Generated from Smithy shape ``com.amazonaws.lakeformation#VirtualObjectList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.virtual_object

VirtualObjectList: TypeAlias = list[
    "aws_sdk_lakeformation.types.virtual_object.VirtualObject"
]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualObjectList) -> list:
    import aws_sdk_lakeformation.types.virtual_object

    out: list = []
    for item in value:
        out.append(aws_sdk_lakeformation.types.virtual_object.serialize_json(item))
    return out


def deserialize_json(data: list) -> VirtualObjectList:
    import aws_sdk_lakeformation.types.virtual_object

    out: VirtualObjectList = []
    for item in data:
        out.append(aws_sdk_lakeformation.types.virtual_object.deserialize_json(item))
    return out
