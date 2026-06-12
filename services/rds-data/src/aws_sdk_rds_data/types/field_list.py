"""Generated from Smithy shape ``com.amazonaws.rdsdata#FieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.field

FieldList: TypeAlias = list["aws_sdk_rds_data.types.field.Field"]


# --- restJson1 ser/de ---
def serialize_json(value: FieldList) -> list:
    import aws_sdk_rds_data.types.field

    out: list = []
    for item in value:
        out.append(aws_sdk_rds_data.types.field.serialize_json(item))
    return out


def deserialize_json(data: list) -> FieldList:
    import aws_sdk_rds_data.types.field

    out: FieldList = []
    for item in data:
        out.append(aws_sdk_rds_data.types.field.deserialize_json(item))
    return out
