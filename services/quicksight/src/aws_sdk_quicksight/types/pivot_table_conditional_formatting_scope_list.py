"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableConditionalFormattingScopeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope

PivotTableConditionalFormattingScopeList: TypeAlias = list[
    "aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope.PivotTableConditionalFormattingScope"
]


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableConditionalFormattingScopeList) -> list:
    import aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PivotTableConditionalFormattingScopeList:
    import aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope

    out: PivotTableConditionalFormattingScopeList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope.deserialize_json(
                item
            )
        )
    return out
