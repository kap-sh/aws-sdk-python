"""Generated from Smithy shape ``com.amazonaws.quicksight#CascadingControlSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.cascading_control_source

CascadingControlSourceList: TypeAlias = list[
    "aws_sdk_quicksight.types.cascading_control_source.CascadingControlSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: CascadingControlSourceList) -> list:
    import aws_sdk_quicksight.types.cascading_control_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.cascading_control_source.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CascadingControlSourceList:
    import aws_sdk_quicksight.types.cascading_control_source

    out: CascadingControlSourceList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.cascading_control_source.deserialize_json(item)
        )
    return out
