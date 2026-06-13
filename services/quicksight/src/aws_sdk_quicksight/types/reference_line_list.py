"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.reference_line

ReferenceLineList: TypeAlias = list[
    "aws_sdk_quicksight.types.reference_line.ReferenceLine"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLineList) -> list:
    import aws_sdk_quicksight.types.reference_line

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.reference_line.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReferenceLineList:
    import aws_sdk_quicksight.types.reference_line

    out: ReferenceLineList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.reference_line.deserialize_json(item))
    return out
