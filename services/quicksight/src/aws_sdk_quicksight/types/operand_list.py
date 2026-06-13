"""Generated from Smithy shape ``com.amazonaws.quicksight#OperandList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.identifier

OperandList: TypeAlias = list["aws_sdk_quicksight.types.identifier.Identifier"]


# --- restJson1 ser/de ---
def serialize_json(value: OperandList) -> list:
    import aws_sdk_quicksight.types.identifier

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> OperandList:
    import aws_sdk_quicksight.types.identifier

    out: OperandList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.identifier.deserialize_json(item))
    return out
