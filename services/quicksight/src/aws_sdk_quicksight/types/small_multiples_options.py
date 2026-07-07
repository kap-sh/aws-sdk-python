"""Generated from Smithy shape ``com.amazonaws.quicksight#SmallMultiplesOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.panel_configuration
    import aws_sdk_quicksight.types.small_multiples_axis_properties
    import aws_sdk_quicksight.types.visible_panel_columns
    import aws_sdk_quicksight.types.visible_panel_rows


class SmallMultiplesOptions(TypedDict, closed=True):
    max_visible_rows: NotRequired[
        "aws_sdk_quicksight.types.visible_panel_rows.VisiblePanelRows"
    ]
    """<p>Sets the maximum number of visible rows to display in the grid of small multiples panels.</p> <p>The default value is <code>Auto</code>, which automatically adjusts the rows in the grid to fit the overall layout and size of the given chart.</p>"""
    max_visible_columns: NotRequired[
        "aws_sdk_quicksight.types.visible_panel_columns.VisiblePanelColumns"
    ]
    """<p>Sets the maximum number of visible columns to display in the grid of small multiples panels.</p> <p>The default is <code>Auto</code>, which automatically adjusts the columns in the grid to fit the overall layout and size of the given chart.</p>"""
    panel_configuration: NotRequired[
        "aws_sdk_quicksight.types.panel_configuration.PanelConfiguration"
    ]
    """<p>Configures the display options for each small multiples panel.</p>"""
    x_axis: NotRequired[
        "aws_sdk_quicksight.types.small_multiples_axis_properties.SmallMultiplesAxisProperties"
    ]
    """<p>The properties of a small multiples X axis.</p>"""
    y_axis: NotRequired[
        "aws_sdk_quicksight.types.small_multiples_axis_properties.SmallMultiplesAxisProperties"
    ]
    """<p>The properties of a small multiples Y axis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SmallMultiplesOptions) -> dict:
    out: dict = {}
    if "max_visible_rows" in value:
        out["MaxVisibleRows"] = value["max_visible_rows"]
    if "max_visible_columns" in value:
        out["MaxVisibleColumns"] = value["max_visible_columns"]
    if "panel_configuration" in value:
        import aws_sdk_quicksight.types.panel_configuration

        out["PanelConfiguration"] = (
            aws_sdk_quicksight.types.panel_configuration.serialize_json(
                value["panel_configuration"]
            )
        )
    if "x_axis" in value:
        import aws_sdk_quicksight.types.small_multiples_axis_properties

        out["XAxis"] = (
            aws_sdk_quicksight.types.small_multiples_axis_properties.serialize_json(
                value["x_axis"]
            )
        )
    if "y_axis" in value:
        import aws_sdk_quicksight.types.small_multiples_axis_properties

        out["YAxis"] = (
            aws_sdk_quicksight.types.small_multiples_axis_properties.serialize_json(
                value["y_axis"]
            )
        )
    return out


def deserialize_json(data: dict) -> SmallMultiplesOptions:
    out: SmallMultiplesOptions = {}  # type: ignore[typeddict-item]
    if "MaxVisibleRows" in data:
        out["max_visible_rows"] = data["MaxVisibleRows"]
    if "MaxVisibleColumns" in data:
        out["max_visible_columns"] = data["MaxVisibleColumns"]
    if "PanelConfiguration" in data:
        import aws_sdk_quicksight.types.panel_configuration

        out["panel_configuration"] = (
            aws_sdk_quicksight.types.panel_configuration.deserialize_json(
                data["PanelConfiguration"]
            )
        )
    if "XAxis" in data:
        import aws_sdk_quicksight.types.small_multiples_axis_properties

        out["x_axis"] = (
            aws_sdk_quicksight.types.small_multiples_axis_properties.deserialize_json(
                data["XAxis"]
            )
        )
    if "YAxis" in data:
        import aws_sdk_quicksight.types.small_multiples_axis_properties

        out["y_axis"] = (
            aws_sdk_quicksight.types.small_multiples_axis_properties.deserialize_json(
                data["YAxis"]
            )
        )
    return out
