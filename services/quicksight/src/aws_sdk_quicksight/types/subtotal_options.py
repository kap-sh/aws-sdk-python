"""Generated from Smithy shape ``com.amazonaws.quicksight#SubtotalOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pivot_table_field_subtotal_options_list
    import aws_sdk_quicksight.types.pivot_table_subtotal_level
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.table_cell_style
    import aws_sdk_quicksight.types.table_style_target_list
    import aws_sdk_quicksight.types.visibility


class SubtotalOptions(TypedDict, closed=True):
    totals_visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The visibility configuration for the subtotal cells.</p>"""
    custom_label: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The custom label string for the subtotal cells.</p>"""
    field_level: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_subtotal_level.PivotTableSubtotalLevel"
    ]
    """<p>The field level (all, custom, last) for the subtotal cells.</p>"""
    field_level_options: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_field_subtotal_options_list.PivotTableFieldSubtotalOptionsList"
    ]
    """<p>The optional configuration of subtotal cells.</p>"""
    total_cell_style: NotRequired[
        "aws_sdk_quicksight.types.table_cell_style.TableCellStyle"
    ]
    """<p>The cell styling options for the subtotal cells.</p>"""
    value_cell_style: NotRequired[
        "aws_sdk_quicksight.types.table_cell_style.TableCellStyle"
    ]
    """<p>The cell styling options for the subtotals of value cells.</p>"""
    metric_header_cell_style: NotRequired[
        "aws_sdk_quicksight.types.table_cell_style.TableCellStyle"
    ]
    """<p>The cell styling options for the subtotals of header cells.</p>"""
    style_targets: NotRequired[
        "aws_sdk_quicksight.types.table_style_target_list.TableStyleTargetList"
    ]
    """<p>The style targets options for subtotals.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubtotalOptions) -> dict:
    out: dict = {}
    if "totals_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["TotalsVisibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["totals_visibility"]
        )
    if "custom_label" in value:
        out["CustomLabel"] = value["custom_label"]
    if "field_level" in value:
        import aws_sdk_quicksight.types.pivot_table_subtotal_level

        out["FieldLevel"] = (
            aws_sdk_quicksight.types.pivot_table_subtotal_level.serialize_json(
                value["field_level"]
            )
        )
    if "field_level_options" in value:
        import aws_sdk_quicksight.types.pivot_table_field_subtotal_options_list

        out["FieldLevelOptions"] = (
            aws_sdk_quicksight.types.pivot_table_field_subtotal_options_list.serialize_json(
                value["field_level_options"]
            )
        )
    if "total_cell_style" in value:
        import aws_sdk_quicksight.types.table_cell_style

        out["TotalCellStyle"] = (
            aws_sdk_quicksight.types.table_cell_style.serialize_json(
                value["total_cell_style"]
            )
        )
    if "value_cell_style" in value:
        import aws_sdk_quicksight.types.table_cell_style

        out["ValueCellStyle"] = (
            aws_sdk_quicksight.types.table_cell_style.serialize_json(
                value["value_cell_style"]
            )
        )
    if "metric_header_cell_style" in value:
        import aws_sdk_quicksight.types.table_cell_style

        out["MetricHeaderCellStyle"] = (
            aws_sdk_quicksight.types.table_cell_style.serialize_json(
                value["metric_header_cell_style"]
            )
        )
    if "style_targets" in value:
        import aws_sdk_quicksight.types.table_style_target_list

        out["StyleTargets"] = (
            aws_sdk_quicksight.types.table_style_target_list.serialize_json(
                value["style_targets"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubtotalOptions:
    out: SubtotalOptions = {}  # type: ignore[typeddict-item]
    if "TotalsVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["totals_visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["TotalsVisibility"]
        )
    if "CustomLabel" in data:
        out["custom_label"] = data["CustomLabel"]
    if "FieldLevel" in data:
        import aws_sdk_quicksight.types.pivot_table_subtotal_level

        out["field_level"] = (
            aws_sdk_quicksight.types.pivot_table_subtotal_level.deserialize_json(
                data["FieldLevel"]
            )
        )
    if "FieldLevelOptions" in data:
        import aws_sdk_quicksight.types.pivot_table_field_subtotal_options_list

        out["field_level_options"] = (
            aws_sdk_quicksight.types.pivot_table_field_subtotal_options_list.deserialize_json(
                data["FieldLevelOptions"]
            )
        )
    if "TotalCellStyle" in data:
        import aws_sdk_quicksight.types.table_cell_style

        out["total_cell_style"] = (
            aws_sdk_quicksight.types.table_cell_style.deserialize_json(
                data["TotalCellStyle"]
            )
        )
    if "ValueCellStyle" in data:
        import aws_sdk_quicksight.types.table_cell_style

        out["value_cell_style"] = (
            aws_sdk_quicksight.types.table_cell_style.deserialize_json(
                data["ValueCellStyle"]
            )
        )
    if "MetricHeaderCellStyle" in data:
        import aws_sdk_quicksight.types.table_cell_style

        out["metric_header_cell_style"] = (
            aws_sdk_quicksight.types.table_cell_style.deserialize_json(
                data["MetricHeaderCellStyle"]
            )
        )
    if "StyleTargets" in data:
        import aws_sdk_quicksight.types.table_style_target_list

        out["style_targets"] = (
            aws_sdk_quicksight.types.table_style_target_list.deserialize_json(
                data["StyleTargets"]
            )
        )
    return out
