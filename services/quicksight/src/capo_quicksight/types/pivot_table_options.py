"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_table_metric_placement
    import capo_quicksight.types.pivot_table_rows_label_options
    import capo_quicksight.types.pivot_table_rows_layout
    import capo_quicksight.types.pixel_length
    import capo_quicksight.types.row_alternate_color_options
    import capo_quicksight.types.table_cell_style
    import capo_quicksight.types.visibility


class PivotTableOptions(TypedDict, closed=True):
    metric_placement: NotRequired[
        "capo_quicksight.types.pivot_table_metric_placement.PivotTableMetricPlacement"
    ]
    """<p>The metric placement (row, column) options.</p>"""
    single_metric_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the single metric options.</p>"""
    column_names_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the column names.</p>"""
    toggle_buttons_visibility: NotRequired[
        "capo_quicksight.types.visibility.Visibility"
    ]
    """<p>Determines the visibility of the pivot table.</p>"""
    column_header_style: NotRequired[
        "capo_quicksight.types.table_cell_style.TableCellStyle"
    ]
    """<p>The table cell style of the column header.</p>"""
    row_header_style: NotRequired[
        "capo_quicksight.types.table_cell_style.TableCellStyle"
    ]
    """<p>The table cell style of the row headers.</p>"""
    cell_style: NotRequired["capo_quicksight.types.table_cell_style.TableCellStyle"]
    """<p>The table cell style of cells.</p>"""
    row_field_names_style: NotRequired[
        "capo_quicksight.types.table_cell_style.TableCellStyle"
    ]
    """<p>The table cell style of row field names.</p>"""
    row_alternate_color_options: NotRequired[
        "capo_quicksight.types.row_alternate_color_options.RowAlternateColorOptions"
    ]
    """<p>The row alternate color options (widget status, row alternate colors).</p>"""
    collapsed_row_dimensions_visibility: NotRequired[
        "capo_quicksight.types.visibility.Visibility"
    ]
    """<p>The visibility setting of a pivot table's collapsed row dimension fields. If the value of this structure is <code>HIDDEN</code>, all collapsed columns in a pivot table are automatically hidden. The default value is <code>VISIBLE</code>.</p>"""
    rows_layout: NotRequired[
        "capo_quicksight.types.pivot_table_rows_layout.PivotTableRowsLayout"
    ]
    """<p>The layout for the row dimension headers of a pivot table. Choose one of the following options.</p> <ul> <li> <p> <code>TABULAR</code>: (Default) Each row field is displayed in a separate column.</p> </li> <li> <p> <code>HIERARCHY</code>: All row fields are displayed in a single column. Indentation is used to differentiate row headers of different fields.</p> </li> </ul>"""
    rows_label_options: NotRequired[
        "capo_quicksight.types.pivot_table_rows_label_options.PivotTableRowsLabelOptions"
    ]
    """<p>The options for the label that is located above the row headers. This option is only applicable when <code>RowsLayout</code> is set to <code>HIERARCHY</code>.</p>"""
    default_cell_width: NotRequired["capo_quicksight.types.pixel_length.PixelLength"]
    """<p>The default cell width of the pivot table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableOptions) -> dict:
    out: dict = {}
    if "metric_placement" in value:
        import capo_quicksight.types.pivot_table_metric_placement

        out["MetricPlacement"] = (
            capo_quicksight.types.pivot_table_metric_placement.serialize_json(
                value["metric_placement"]
            )
        )
    if "single_metric_visibility" in value:
        import capo_quicksight.types.visibility

        out["SingleMetricVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["single_metric_visibility"]
        )
    if "column_names_visibility" in value:
        import capo_quicksight.types.visibility

        out["ColumnNamesVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["column_names_visibility"]
        )
    if "toggle_buttons_visibility" in value:
        import capo_quicksight.types.visibility

        out["ToggleButtonsVisibility"] = (
            capo_quicksight.types.visibility.serialize_json(
                value["toggle_buttons_visibility"]
            )
        )
    if "column_header_style" in value:
        import capo_quicksight.types.table_cell_style

        out["ColumnHeaderStyle"] = (
            capo_quicksight.types.table_cell_style.serialize_json(
                value["column_header_style"]
            )
        )
    if "row_header_style" in value:
        import capo_quicksight.types.table_cell_style

        out["RowHeaderStyle"] = capo_quicksight.types.table_cell_style.serialize_json(
            value["row_header_style"]
        )
    if "cell_style" in value:
        import capo_quicksight.types.table_cell_style

        out["CellStyle"] = capo_quicksight.types.table_cell_style.serialize_json(
            value["cell_style"]
        )
    if "row_field_names_style" in value:
        import capo_quicksight.types.table_cell_style

        out["RowFieldNamesStyle"] = (
            capo_quicksight.types.table_cell_style.serialize_json(
                value["row_field_names_style"]
            )
        )
    if "row_alternate_color_options" in value:
        import capo_quicksight.types.row_alternate_color_options

        out["RowAlternateColorOptions"] = (
            capo_quicksight.types.row_alternate_color_options.serialize_json(
                value["row_alternate_color_options"]
            )
        )
    if "collapsed_row_dimensions_visibility" in value:
        import capo_quicksight.types.visibility

        out["CollapsedRowDimensionsVisibility"] = (
            capo_quicksight.types.visibility.serialize_json(
                value["collapsed_row_dimensions_visibility"]
            )
        )
    if "rows_layout" in value:
        import capo_quicksight.types.pivot_table_rows_layout

        out["RowsLayout"] = (
            capo_quicksight.types.pivot_table_rows_layout.serialize_json(
                value["rows_layout"]
            )
        )
    if "rows_label_options" in value:
        import capo_quicksight.types.pivot_table_rows_label_options

        out["RowsLabelOptions"] = (
            capo_quicksight.types.pivot_table_rows_label_options.serialize_json(
                value["rows_label_options"]
            )
        )
    if "default_cell_width" in value:
        out["DefaultCellWidth"] = value["default_cell_width"]
    return out


def deserialize_json(data: dict) -> PivotTableOptions:
    out: PivotTableOptions = {}  # type: ignore[typeddict-item]
    if "MetricPlacement" in data:
        import capo_quicksight.types.pivot_table_metric_placement

        out["metric_placement"] = (
            capo_quicksight.types.pivot_table_metric_placement.deserialize_json(
                data["MetricPlacement"]
            )
        )
    if "SingleMetricVisibility" in data:
        import capo_quicksight.types.visibility

        out["single_metric_visibility"] = (
            capo_quicksight.types.visibility.deserialize_json(
                data["SingleMetricVisibility"]
            )
        )
    if "ColumnNamesVisibility" in data:
        import capo_quicksight.types.visibility

        out["column_names_visibility"] = (
            capo_quicksight.types.visibility.deserialize_json(
                data["ColumnNamesVisibility"]
            )
        )
    if "ToggleButtonsVisibility" in data:
        import capo_quicksight.types.visibility

        out["toggle_buttons_visibility"] = (
            capo_quicksight.types.visibility.deserialize_json(
                data["ToggleButtonsVisibility"]
            )
        )
    if "ColumnHeaderStyle" in data:
        import capo_quicksight.types.table_cell_style

        out["column_header_style"] = (
            capo_quicksight.types.table_cell_style.deserialize_json(
                data["ColumnHeaderStyle"]
            )
        )
    if "RowHeaderStyle" in data:
        import capo_quicksight.types.table_cell_style

        out["row_header_style"] = (
            capo_quicksight.types.table_cell_style.deserialize_json(
                data["RowHeaderStyle"]
            )
        )
    if "CellStyle" in data:
        import capo_quicksight.types.table_cell_style

        out["cell_style"] = capo_quicksight.types.table_cell_style.deserialize_json(
            data["CellStyle"]
        )
    if "RowFieldNamesStyle" in data:
        import capo_quicksight.types.table_cell_style

        out["row_field_names_style"] = (
            capo_quicksight.types.table_cell_style.deserialize_json(
                data["RowFieldNamesStyle"]
            )
        )
    if "RowAlternateColorOptions" in data:
        import capo_quicksight.types.row_alternate_color_options

        out["row_alternate_color_options"] = (
            capo_quicksight.types.row_alternate_color_options.deserialize_json(
                data["RowAlternateColorOptions"]
            )
        )
    if "CollapsedRowDimensionsVisibility" in data:
        import capo_quicksight.types.visibility

        out["collapsed_row_dimensions_visibility"] = (
            capo_quicksight.types.visibility.deserialize_json(
                data["CollapsedRowDimensionsVisibility"]
            )
        )
    if "RowsLayout" in data:
        import capo_quicksight.types.pivot_table_rows_layout

        out["rows_layout"] = (
            capo_quicksight.types.pivot_table_rows_layout.deserialize_json(
                data["RowsLayout"]
            )
        )
    if "RowsLabelOptions" in data:
        import capo_quicksight.types.pivot_table_rows_label_options

        out["rows_label_options"] = (
            capo_quicksight.types.pivot_table_rows_label_options.deserialize_json(
                data["RowsLabelOptions"]
            )
        )
    if "DefaultCellWidth" in data:
        out["default_cell_width"] = data["DefaultCellWidth"]
    return out
