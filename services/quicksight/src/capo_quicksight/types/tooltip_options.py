"""Generated from Smithy shape ``com.amazonaws.quicksight#TooltipOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.field_based_tooltip
    import capo_quicksight.types.selected_tooltip_type
    import capo_quicksight.types.sheet_tooltip
    import capo_quicksight.types.visibility


class TooltipOptions(TypedDict, closed=True):
    tooltip_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>Determines whether or not the tooltip is visible.</p>"""
    selected_tooltip_type: NotRequired[
        "capo_quicksight.types.selected_tooltip_type.SelectedTooltipType"
    ]
    """<p>The selected type for the tooltip. Choose one of the following options:</p> <ul> <li> <p> <code>BASIC</code>: A basic tooltip.</p> </li> <li> <p> <code>DETAILED</code>: A detailed tooltip.</p> </li> </ul>"""
    field_based_tooltip: NotRequired[
        "capo_quicksight.types.field_based_tooltip.FieldBasedTooltip"
    ]
    """<p>The setup for the detailed tooltip. The tooltip setup is always saved. The display type is decided based on the tooltip type.</p>"""
    sheet_tooltip: NotRequired["capo_quicksight.types.sheet_tooltip.SheetTooltip"]


# --- restJson1 ser/de ---
def serialize_json(value: TooltipOptions) -> dict:
    out: dict = {}
    if "tooltip_visibility" in value:
        import capo_quicksight.types.visibility

        out["TooltipVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["tooltip_visibility"]
        )
    if "selected_tooltip_type" in value:
        import capo_quicksight.types.selected_tooltip_type

        out["SelectedTooltipType"] = (
            capo_quicksight.types.selected_tooltip_type.serialize_json(
                value["selected_tooltip_type"]
            )
        )
    if "field_based_tooltip" in value:
        import capo_quicksight.types.field_based_tooltip

        out["FieldBasedTooltip"] = (
            capo_quicksight.types.field_based_tooltip.serialize_json(
                value["field_based_tooltip"]
            )
        )
    if "sheet_tooltip" in value:
        import capo_quicksight.types.sheet_tooltip

        out["SheetTooltip"] = capo_quicksight.types.sheet_tooltip.serialize_json(
            value["sheet_tooltip"]
        )
    return out


def deserialize_json(data: dict) -> TooltipOptions:
    out: TooltipOptions = {}  # type: ignore[typeddict-item]
    if "TooltipVisibility" in data:
        import capo_quicksight.types.visibility

        out["tooltip_visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["TooltipVisibility"]
        )
    if "SelectedTooltipType" in data:
        import capo_quicksight.types.selected_tooltip_type

        out["selected_tooltip_type"] = (
            capo_quicksight.types.selected_tooltip_type.deserialize_json(
                data["SelectedTooltipType"]
            )
        )
    if "FieldBasedTooltip" in data:
        import capo_quicksight.types.field_based_tooltip

        out["field_based_tooltip"] = (
            capo_quicksight.types.field_based_tooltip.deserialize_json(
                data["FieldBasedTooltip"]
            )
        )
    if "SheetTooltip" in data:
        import capo_quicksight.types.sheet_tooltip

        out["sheet_tooltip"] = capo_quicksight.types.sheet_tooltip.deserialize_json(
            data["SheetTooltip"]
        )
    return out
