"""Generated from Smithy shape ``com.amazonaws.connect#FieldValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.field_value

FieldValues: TypeAlias = list["aws_sdk_connect.types.field_value.FieldValue"]


# --- restJson1 ser/de ---
def serialize_json(value: FieldValues) -> list:
    import aws_sdk_connect.types.field_value

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.field_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> FieldValues:
    import aws_sdk_connect.types.field_value

    out: FieldValues = []
    for item in data:
        out.append(aws_sdk_connect.types.field_value.deserialize_json(item))
    return out
