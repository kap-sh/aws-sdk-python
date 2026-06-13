"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableConditionalFormattingScope``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope_role


class PivotTableConditionalFormattingScope(TypedDict):
    role: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope_role.PivotTableConditionalFormattingScopeRole"
    ]
    """<p>The role (field, field total, grand total) of the cell for conditional formatting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableConditionalFormattingScope) -> dict:
    out: dict = {}
    if "role" in value:
        import aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope_role

        out["Role"] = (
            aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope_role.serialize_json(
                value["role"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableConditionalFormattingScope:
    out: PivotTableConditionalFormattingScope = {}  # type: ignore[typeddict-item]
    if "Role" in data:
        import aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope_role

        out["role"] = (
            aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope_role.deserialize_json(
                data["Role"]
            )
        )
    return out
