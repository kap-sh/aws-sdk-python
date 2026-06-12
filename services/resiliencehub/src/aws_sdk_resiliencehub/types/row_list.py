"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.row

RowList: TypeAlias = list["aws_sdk_resiliencehub.types.row.Row"]


# --- restJson1 ser/de ---
def serialize_json(value: RowList) -> list:
    import aws_sdk_resiliencehub.types.row

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehub.types.row.serialize_json(item))
    return out


def deserialize_json(data: list) -> RowList:
    import aws_sdk_resiliencehub.types.row

    out: RowList = []
    for item in data:
        out.append(aws_sdk_resiliencehub.types.row.deserialize_json(item))
    return out
