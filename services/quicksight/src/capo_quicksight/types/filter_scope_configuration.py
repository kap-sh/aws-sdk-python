"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterScopeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.all_sheets_filter_scope_configuration
    import capo_quicksight.types.selected_sheets_filter_scope_configuration


class FilterScopeConfiguration(TypedDict, closed=True):
    selected_sheets: NotRequired[
        "capo_quicksight.types.selected_sheets_filter_scope_configuration.SelectedSheetsFilterScopeConfiguration"
    ]
    """<p>The configuration for applying a filter to specific sheets.</p>"""
    all_sheets: NotRequired[
        "capo_quicksight.types.all_sheets_filter_scope_configuration.AllSheetsFilterScopeConfiguration"
    ]
    """<p>The configuration that applies a filter to all sheets. When you choose <code>AllSheets</code> as the value for a <code>FilterScopeConfiguration</code>, this filter is applied to all visuals of all sheets in an Analysis, Dashboard, or Template. The <code>AllSheetsFilterScopeConfiguration</code> is chosen.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterScopeConfiguration) -> dict:
    out: dict = {}
    if "selected_sheets" in value:
        import capo_quicksight.types.selected_sheets_filter_scope_configuration

        out["SelectedSheets"] = (
            capo_quicksight.types.selected_sheets_filter_scope_configuration.serialize_json(
                value["selected_sheets"]
            )
        )
    if "all_sheets" in value:
        import capo_quicksight.types.all_sheets_filter_scope_configuration

        out["AllSheets"] = (
            capo_quicksight.types.all_sheets_filter_scope_configuration.serialize_json(
                value["all_sheets"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterScopeConfiguration:
    out: FilterScopeConfiguration = {}  # type: ignore[typeddict-item]
    if "SelectedSheets" in data:
        import capo_quicksight.types.selected_sheets_filter_scope_configuration

        out["selected_sheets"] = (
            capo_quicksight.types.selected_sheets_filter_scope_configuration.deserialize_json(
                data["SelectedSheets"]
            )
        )
    if "AllSheets" in data:
        import capo_quicksight.types.all_sheets_filter_scope_configuration

        out["all_sheets"] = (
            capo_quicksight.types.all_sheets_filter_scope_configuration.deserialize_json(
                data["AllSheets"]
            )
        )
    return out
