"""Generated from Smithy shape ``com.amazonaws.quicksight#CalculatedFieldReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.identifier

CalculatedFieldReferenceList: TypeAlias = list[
    "aws_sdk_quicksight.types.identifier.Identifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedFieldReferenceList) -> list:
    import aws_sdk_quicksight.types.identifier

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> CalculatedFieldReferenceList:
    import aws_sdk_quicksight.types.identifier

    out: CalculatedFieldReferenceList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.identifier.deserialize_json(item))
    return out
