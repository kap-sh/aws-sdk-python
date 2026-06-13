"""Generated from Smithy shape ``com.amazonaws.quicksight#UnaggregatedFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.unaggregated_field

UnaggregatedFieldList: TypeAlias = list[
    "aws_sdk_quicksight.types.unaggregated_field.UnaggregatedField"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnaggregatedFieldList) -> list:
    import aws_sdk_quicksight.types.unaggregated_field

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.unaggregated_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> UnaggregatedFieldList:
    import aws_sdk_quicksight.types.unaggregated_field

    out: UnaggregatedFieldList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.unaggregated_field.deserialize_json(item))
    return out
