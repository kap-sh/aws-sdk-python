"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ColumnsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.column_info

ColumnsList: TypeAlias = list["aws_sdk_iotsitewise.types.column_info.ColumnInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnsList) -> list:
    import aws_sdk_iotsitewise.types.column_info

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.column_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnsList:
    import aws_sdk_iotsitewise.types.column_info

    out: ColumnsList = []
    for item in data:
        out.append(aws_sdk_iotsitewise.types.column_info.deserialize_json(item))
    return out
