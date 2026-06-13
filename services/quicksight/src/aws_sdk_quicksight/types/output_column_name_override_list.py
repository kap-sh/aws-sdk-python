"""Generated from Smithy shape ``com.amazonaws.quicksight#OutputColumnNameOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.output_column_name_override

OutputColumnNameOverrideList: TypeAlias = list[
    "aws_sdk_quicksight.types.output_column_name_override.OutputColumnNameOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputColumnNameOverrideList) -> list:
    import aws_sdk_quicksight.types.output_column_name_override

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.output_column_name_override.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OutputColumnNameOverrideList:
    import aws_sdk_quicksight.types.output_column_name_override

    out: OutputColumnNameOverrideList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.output_column_name_override.deserialize_json(item)
        )
    return out
