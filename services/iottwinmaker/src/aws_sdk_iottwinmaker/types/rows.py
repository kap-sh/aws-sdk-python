"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#Rows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.row

Rows: TypeAlias = list["aws_sdk_iottwinmaker.types.row.Row"]


# --- restJson1 ser/de ---
def serialize_json(value: Rows) -> list:
    import aws_sdk_iottwinmaker.types.row

    out: list = []
    for item in value:
        out.append(aws_sdk_iottwinmaker.types.row.serialize_json(item))
    return out


def deserialize_json(data: list) -> Rows:
    import aws_sdk_iottwinmaker.types.row

    out: Rows = []
    for item in data:
        out.append(aws_sdk_iottwinmaker.types.row.deserialize_json(item))
    return out
