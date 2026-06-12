"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Rows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.row

Rows: TypeAlias = list["aws_sdk_iotsitewise.types.row.Row"]


# --- restJson1 ser/de ---
def serialize_json(value: Rows) -> list:
    import aws_sdk_iotsitewise.types.row

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.row.serialize_json(item))
    return out


def deserialize_json(data: list) -> Rows:
    import aws_sdk_iotsitewise.types.row

    out: Rows = []
    for item in data:
        out.append(aws_sdk_iotsitewise.types.row.deserialize_json(item))
    return out
