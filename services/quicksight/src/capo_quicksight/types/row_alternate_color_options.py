"""Generated from Smithy shape ``com.amazonaws.quicksight#RowAlternateColorOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.row_alternate_color_list
    import capo_quicksight.types.widget_status


class RowAlternateColorOptions(TypedDict, closed=True):
    status: NotRequired["capo_quicksight.types.widget_status.WidgetStatus"]
    """<p>Determines the widget status.</p>"""
    row_alternate_colors: NotRequired[
        "capo_quicksight.types.row_alternate_color_list.RowAlternateColorList"
    ]
    """<p>Determines the list of row alternate colors.</p>"""
    use_primary_background_color: NotRequired[
        "capo_quicksight.types.widget_status.WidgetStatus"
    ]
    """<p>The primary background color options for alternate rows.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RowAlternateColorOptions) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_quicksight.types.widget_status

        out["Status"] = capo_quicksight.types.widget_status.serialize_json(
            value["status"]
        )
    if "row_alternate_colors" in value:
        import capo_quicksight.types.row_alternate_color_list

        out["RowAlternateColors"] = (
            capo_quicksight.types.row_alternate_color_list.serialize_json(
                value["row_alternate_colors"]
            )
        )
    if "use_primary_background_color" in value:
        import capo_quicksight.types.widget_status

        out["UsePrimaryBackgroundColor"] = (
            capo_quicksight.types.widget_status.serialize_json(
                value["use_primary_background_color"]
            )
        )
    return out


def deserialize_json(data: dict) -> RowAlternateColorOptions:
    out: RowAlternateColorOptions = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_quicksight.types.widget_status

        out["status"] = capo_quicksight.types.widget_status.deserialize_json(
            data["Status"]
        )
    if "RowAlternateColors" in data:
        import capo_quicksight.types.row_alternate_color_list

        out["row_alternate_colors"] = (
            capo_quicksight.types.row_alternate_color_list.deserialize_json(
                data["RowAlternateColors"]
            )
        )
    if "UsePrimaryBackgroundColor" in data:
        import capo_quicksight.types.widget_status

        out["use_primary_background_color"] = (
            capo_quicksight.types.widget_status.deserialize_json(
                data["UsePrimaryBackgroundColor"]
            )
        )
    return out
