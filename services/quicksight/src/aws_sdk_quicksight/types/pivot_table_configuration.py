"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dashboard_customization_visual_options
    import aws_sdk_quicksight.types.pivot_table_field_options
    import aws_sdk_quicksight.types.pivot_table_field_wells
    import aws_sdk_quicksight.types.pivot_table_options
    import aws_sdk_quicksight.types.pivot_table_paginated_report_options
    import aws_sdk_quicksight.types.pivot_table_sort_configuration
    import aws_sdk_quicksight.types.pivot_table_total_options
    import aws_sdk_quicksight.types.tooltip_options
    import aws_sdk_quicksight.types.visual_interaction_options


class PivotTableConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_field_wells.PivotTableFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_sort_configuration.PivotTableSortConfiguration"
    ]
    """<p>The sort configuration for a <code>PivotTableVisual</code>.</p>"""
    table_options: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_options.PivotTableOptions"
    ]
    """<p>The table options for a pivot table visual.</p>"""
    total_options: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_total_options.PivotTableTotalOptions"
    ]
    """<p>The total options for a pivot table visual.</p>"""
    field_options: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_field_options.PivotTableFieldOptions"
    ]
    """<p>The field options for a pivot table visual.</p>"""
    paginated_report_options: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_paginated_report_options.PivotTablePaginatedReportOptions"
    ]
    """<p>The paginated report options for a pivot table visual.</p>"""
    tooltip: NotRequired["aws_sdk_quicksight.types.tooltip_options.TooltipOptions"]
    dashboard_customization_visual_options: NotRequired[
        "aws_sdk_quicksight.types.dashboard_customization_visual_options.DashboardCustomizationVisualOptions"
    ]
    """<p>The options that define customizations available to dashboard readers for a specific visual</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import aws_sdk_quicksight.types.pivot_table_field_wells

        out["FieldWells"] = (
            aws_sdk_quicksight.types.pivot_table_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import aws_sdk_quicksight.types.pivot_table_sort_configuration

        out["SortConfiguration"] = (
            aws_sdk_quicksight.types.pivot_table_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "table_options" in value:
        import aws_sdk_quicksight.types.pivot_table_options

        out["TableOptions"] = (
            aws_sdk_quicksight.types.pivot_table_options.serialize_json(
                value["table_options"]
            )
        )
    if "total_options" in value:
        import aws_sdk_quicksight.types.pivot_table_total_options

        out["TotalOptions"] = (
            aws_sdk_quicksight.types.pivot_table_total_options.serialize_json(
                value["total_options"]
            )
        )
    if "field_options" in value:
        import aws_sdk_quicksight.types.pivot_table_field_options

        out["FieldOptions"] = (
            aws_sdk_quicksight.types.pivot_table_field_options.serialize_json(
                value["field_options"]
            )
        )
    if "paginated_report_options" in value:
        import aws_sdk_quicksight.types.pivot_table_paginated_report_options

        out["PaginatedReportOptions"] = (
            aws_sdk_quicksight.types.pivot_table_paginated_report_options.serialize_json(
                value["paginated_report_options"]
            )
        )
    if "tooltip" in value:
        import aws_sdk_quicksight.types.tooltip_options

        out["Tooltip"] = aws_sdk_quicksight.types.tooltip_options.serialize_json(
            value["tooltip"]
        )
    if "dashboard_customization_visual_options" in value:
        import aws_sdk_quicksight.types.dashboard_customization_visual_options

        out["DashboardCustomizationVisualOptions"] = (
            aws_sdk_quicksight.types.dashboard_customization_visual_options.serialize_json(
                value["dashboard_customization_visual_options"]
            )
        )
    if "interactions" in value:
        import aws_sdk_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            aws_sdk_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableConfiguration:
    out: PivotTableConfiguration = {}  # type: ignore[typeddict-item]
    if "FieldWells" in data:
        import aws_sdk_quicksight.types.pivot_table_field_wells

        out["field_wells"] = (
            aws_sdk_quicksight.types.pivot_table_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if "SortConfiguration" in data:
        import aws_sdk_quicksight.types.pivot_table_sort_configuration

        out["sort_configuration"] = (
            aws_sdk_quicksight.types.pivot_table_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if "TableOptions" in data:
        import aws_sdk_quicksight.types.pivot_table_options

        out["table_options"] = (
            aws_sdk_quicksight.types.pivot_table_options.deserialize_json(
                data["TableOptions"]
            )
        )
    if "TotalOptions" in data:
        import aws_sdk_quicksight.types.pivot_table_total_options

        out["total_options"] = (
            aws_sdk_quicksight.types.pivot_table_total_options.deserialize_json(
                data["TotalOptions"]
            )
        )
    if "FieldOptions" in data:
        import aws_sdk_quicksight.types.pivot_table_field_options

        out["field_options"] = (
            aws_sdk_quicksight.types.pivot_table_field_options.deserialize_json(
                data["FieldOptions"]
            )
        )
    if "PaginatedReportOptions" in data:
        import aws_sdk_quicksight.types.pivot_table_paginated_report_options

        out["paginated_report_options"] = (
            aws_sdk_quicksight.types.pivot_table_paginated_report_options.deserialize_json(
                data["PaginatedReportOptions"]
            )
        )
    if "Tooltip" in data:
        import aws_sdk_quicksight.types.tooltip_options

        out["tooltip"] = aws_sdk_quicksight.types.tooltip_options.deserialize_json(
            data["Tooltip"]
        )
    if "DashboardCustomizationVisualOptions" in data:
        import aws_sdk_quicksight.types.dashboard_customization_visual_options

        out["dashboard_customization_visual_options"] = (
            aws_sdk_quicksight.types.dashboard_customization_visual_options.deserialize_json(
                data["DashboardCustomizationVisualOptions"]
            )
        )
    if "Interactions" in data:
        import aws_sdk_quicksight.types.visual_interaction_options

        out["interactions"] = (
            aws_sdk_quicksight.types.visual_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out
