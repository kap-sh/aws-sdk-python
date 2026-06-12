"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_item

FieldList: TypeAlias = list["aws_sdk_connectcases.types.field_item.FieldItem"]


# --- restJson1 ser/de ---
def serialize_json(value: FieldList) -> list:
    import aws_sdk_connectcases.types.field_item

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcases.types.field_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> FieldList:
    import aws_sdk_connectcases.types.field_item

    out: FieldList = []
    for item in data:
        out.append(aws_sdk_connectcases.types.field_item.deserialize_json(item))
    return out
