"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_value

FieldValueList: TypeAlias = list["aws_sdk_connectcases.types.field_value.FieldValue"]


# --- restJson1 ser/de ---
def serialize_json(value: FieldValueList) -> list:
    import aws_sdk_connectcases.types.field_value

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcases.types.field_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> FieldValueList:
    import aws_sdk_connectcases.types.field_value

    out: FieldValueList = []
    for item in data:
        out.append(aws_sdk_connectcases.types.field_value.deserialize_json(item))
    return out
