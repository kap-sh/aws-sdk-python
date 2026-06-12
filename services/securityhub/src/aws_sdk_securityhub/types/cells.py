"""Generated from Smithy shape ``com.amazonaws.securityhub#Cells``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.cell

Cells: TypeAlias = list["aws_sdk_securityhub.types.cell.Cell"]


# --- restJson1 ser/de ---
def serialize_json(value: Cells) -> list:
    import aws_sdk_securityhub.types.cell

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.cell.serialize_json(item))
    return out


def deserialize_json(data: list) -> Cells:
    import aws_sdk_securityhub.types.cell

    out: Cells = []
    for item in data:
        out.append(aws_sdk_securityhub.types.cell.deserialize_json(item))
    return out
