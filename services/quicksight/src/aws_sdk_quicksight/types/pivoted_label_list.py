"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotedLabelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pivoted_label

PivotedLabelList: TypeAlias = list[
    "aws_sdk_quicksight.types.pivoted_label.PivotedLabel"
]


# --- restJson1 ser/de ---
def serialize_json(value: PivotedLabelList) -> list:
    import aws_sdk_quicksight.types.pivoted_label

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.pivoted_label.serialize_json(item))
    return out


def deserialize_json(data: list) -> PivotedLabelList:
    import aws_sdk_quicksight.types.pivoted_label

    out: PivotedLabelList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.pivoted_label.deserialize_json(item))
    return out
