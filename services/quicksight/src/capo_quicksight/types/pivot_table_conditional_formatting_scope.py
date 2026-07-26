"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableConditionalFormattingScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_table_conditional_formatting_scope_role


class PivotTableConditionalFormattingScope(TypedDict, closed=True):
    role: NotRequired[
        "capo_quicksight.types.pivot_table_conditional_formatting_scope_role.PivotTableConditionalFormattingScopeRole"
    ]
    """<p>The role (field, field total, grand total) of the cell for conditional formatting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableConditionalFormattingScope) -> dict:
    out: dict = {}
    if "role" in value:
        import capo_quicksight.types.pivot_table_conditional_formatting_scope_role

        out["Role"] = (
            capo_quicksight.types.pivot_table_conditional_formatting_scope_role.serialize_json(
                value["role"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableConditionalFormattingScope:
    out: PivotTableConditionalFormattingScope = {}  # type: ignore[typeddict-item]
    if "Role" in data:
        import capo_quicksight.types.pivot_table_conditional_formatting_scope_role

        out["role"] = (
            capo_quicksight.types.pivot_table_conditional_formatting_scope_role.deserialize_json(
                data["Role"]
            )
        )
    return out
