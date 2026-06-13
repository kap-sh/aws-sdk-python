"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTotalOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.table_cell_style
    import aws_sdk_quicksight.types.table_totals_placement
    import aws_sdk_quicksight.types.table_totals_scroll_status
    import aws_sdk_quicksight.types.total_aggregation_option_list
    import aws_sdk_quicksight.types.visibility


class PivotTotalOptions(TypedDict):
    totals_visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The visibility configuration for the total cells.</p>"""
    placement: NotRequired[
        "aws_sdk_quicksight.types.table_totals_placement.TableTotalsPlacement"
    ]
    """<p>The placement (start, end) for the total cells.</p>"""
    scroll_status: NotRequired[
        "aws_sdk_quicksight.types.table_totals_scroll_status.TableTotalsScrollStatus"
    ]
    """<p>The scroll status (pinned, scrolled) for the total cells.</p>"""
    custom_label: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The custom label string for the total cells.</p>"""
    total_cell_style: NotRequired[
        "aws_sdk_quicksight.types.table_cell_style.TableCellStyle"
    ]
    """<p>The cell styling options for the total cells.</p>"""
    value_cell_style: NotRequired[
        "aws_sdk_quicksight.types.table_cell_style.TableCellStyle"
    ]
    """<p>The cell styling options for the totals of value cells.</p>"""
    metric_header_cell_style: NotRequired[
        "aws_sdk_quicksight.types.table_cell_style.TableCellStyle"
    ]
    """<p>The cell styling options for the total of header cells.</p>"""
    total_aggregation_options: NotRequired[
        "aws_sdk_quicksight.types.total_aggregation_option_list.TotalAggregationOptionList"
    ]
    """<p>The total aggregation options for each value field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTotalOptions) -> dict:
    out: dict = {}
    if "totals_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["TotalsVisibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["totals_visibility"]
        )
    if "placement" in value:
        import aws_sdk_quicksight.types.table_totals_placement

        out["Placement"] = (
            aws_sdk_quicksight.types.table_totals_placement.serialize_json(
                value["placement"]
            )
        )
    if "scroll_status" in value:
        import aws_sdk_quicksight.types.table_totals_scroll_status

        out["ScrollStatus"] = (
            aws_sdk_quicksight.types.table_totals_scroll_status.serialize_json(
                value["scroll_status"]
            )
        )
    if "custom_label" in value:
        out["CustomLabel"] = value["custom_label"]
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
    if "total_aggregation_options" in value:
        import aws_sdk_quicksight.types.total_aggregation_option_list

        out["TotalAggregationOptions"] = (
            aws_sdk_quicksight.types.total_aggregation_option_list.serialize_json(
                value["total_aggregation_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTotalOptions:
    out: PivotTotalOptions = {}  # type: ignore[typeddict-item]
    if "TotalsVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["totals_visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["TotalsVisibility"]
        )
    if "Placement" in data:
        import aws_sdk_quicksight.types.table_totals_placement

        out["placement"] = (
            aws_sdk_quicksight.types.table_totals_placement.deserialize_json(
                data["Placement"]
            )
        )
    if "ScrollStatus" in data:
        import aws_sdk_quicksight.types.table_totals_scroll_status

        out["scroll_status"] = (
            aws_sdk_quicksight.types.table_totals_scroll_status.deserialize_json(
                data["ScrollStatus"]
            )
        )
    if "CustomLabel" in data:
        out["custom_label"] = data["CustomLabel"]
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
    if "TotalAggregationOptions" in data:
        import aws_sdk_quicksight.types.total_aggregation_option_list

        out["total_aggregation_options"] = (
            aws_sdk_quicksight.types.total_aggregation_option_list.deserialize_json(
                data["TotalAggregationOptions"]
            )
        )
    return out
