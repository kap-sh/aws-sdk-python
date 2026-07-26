"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableRowsLabelOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_table_rows_label_text
    import capo_quicksight.types.visibility


class PivotTableRowsLabelOptions(TypedDict, closed=True):
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the rows label.</p>"""
    custom_label: NotRequired[
        "capo_quicksight.types.pivot_table_rows_label_text.PivotTableRowsLabelText"
    ]
    """<p>The custom label string for the rows label.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableRowsLabelOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "custom_label" in value:
        out["CustomLabel"] = value["custom_label"]
    return out


def deserialize_json(data: dict) -> PivotTableRowsLabelOptions:
    out: PivotTableRowsLabelOptions = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "CustomLabel" in data:
        out["custom_label"] = data["CustomLabel"]
    return out
