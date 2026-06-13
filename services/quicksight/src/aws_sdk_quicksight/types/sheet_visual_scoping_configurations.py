"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetVisualScopingConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sheet_visual_scoping_configuration

SheetVisualScopingConfigurations: TypeAlias = list[
    "aws_sdk_quicksight.types.sheet_visual_scoping_configuration.SheetVisualScopingConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SheetVisualScopingConfigurations) -> list:
    import aws_sdk_quicksight.types.sheet_visual_scoping_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.sheet_visual_scoping_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SheetVisualScopingConfigurations:
    import aws_sdk_quicksight.types.sheet_visual_scoping_configuration

    out: SheetVisualScopingConfigurations = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.sheet_visual_scoping_configuration.deserialize_json(
                item
            )
        )
    return out
