"""Generated from Smithy shape ``com.amazonaws.quicksight#TableConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dashboard_customization_visual_options
    import aws_sdk_quicksight.types.table_field_options
    import aws_sdk_quicksight.types.table_field_wells
    import aws_sdk_quicksight.types.table_inline_visualization_list
    import aws_sdk_quicksight.types.table_options
    import aws_sdk_quicksight.types.table_paginated_report_options
    import aws_sdk_quicksight.types.table_sort_configuration
    import aws_sdk_quicksight.types.tooltip_options
    import aws_sdk_quicksight.types.total_options
    import aws_sdk_quicksight.types.visual_interaction_options


class TableConfiguration(TypedDict):
    field_wells: NotRequired[
        "aws_sdk_quicksight.types.table_field_wells.TableFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "aws_sdk_quicksight.types.table_sort_configuration.TableSortConfiguration"
    ]
    """<p>The sort configuration for a <code>TableVisual</code>.</p>"""
    table_options: NotRequired["aws_sdk_quicksight.types.table_options.TableOptions"]
    """<p>The table options for a table visual.</p>"""
    total_options: NotRequired["aws_sdk_quicksight.types.total_options.TotalOptions"]
    """<p>The total options for a table visual.</p>"""
    field_options: NotRequired[
        "aws_sdk_quicksight.types.table_field_options.TableFieldOptions"
    ]
    """<p>The field options for a table visual.</p>"""
    paginated_report_options: NotRequired[
        "aws_sdk_quicksight.types.table_paginated_report_options.TablePaginatedReportOptions"
    ]
    """<p>The paginated report options for a table visual.</p>"""
    table_inline_visualizations: NotRequired[
        "aws_sdk_quicksight.types.table_inline_visualization_list.TableInlineVisualizationList"
    ]
    """<p>A collection of inline visualizations to display within a chart.</p>"""
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
def serialize_json(value: TableConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import aws_sdk_quicksight.types.table_field_wells

        out["FieldWells"] = aws_sdk_quicksight.types.table_field_wells.serialize_json(
            value["field_wells"]
        )
    if "sort_configuration" in value:
        import aws_sdk_quicksight.types.table_sort_configuration

        out["SortConfiguration"] = (
            aws_sdk_quicksight.types.table_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "table_options" in value:
        import aws_sdk_quicksight.types.table_options

        out["TableOptions"] = aws_sdk_quicksight.types.table_options.serialize_json(
            value["table_options"]
        )
    if "total_options" in value:
        import aws_sdk_quicksight.types.total_options

        out["TotalOptions"] = aws_sdk_quicksight.types.total_options.serialize_json(
            value["total_options"]
        )
    if "field_options" in value:
        import aws_sdk_quicksight.types.table_field_options

        out["FieldOptions"] = (
            aws_sdk_quicksight.types.table_field_options.serialize_json(
                value["field_options"]
            )
        )
    if "paginated_report_options" in value:
        import aws_sdk_quicksight.types.table_paginated_report_options

        out["PaginatedReportOptions"] = (
            aws_sdk_quicksight.types.table_paginated_report_options.serialize_json(
                value["paginated_report_options"]
            )
        )
    if "table_inline_visualizations" in value:
        import aws_sdk_quicksight.types.table_inline_visualization_list

        out["TableInlineVisualizations"] = (
            aws_sdk_quicksight.types.table_inline_visualization_list.serialize_json(
                value["table_inline_visualizations"]
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


def deserialize_json(data: dict) -> TableConfiguration:
    out: TableConfiguration = {}  # type: ignore[typeddict-item]
    if "FieldWells" in data:
        import aws_sdk_quicksight.types.table_field_wells

        out["field_wells"] = (
            aws_sdk_quicksight.types.table_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if "SortConfiguration" in data:
        import aws_sdk_quicksight.types.table_sort_configuration

        out["sort_configuration"] = (
            aws_sdk_quicksight.types.table_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if "TableOptions" in data:
        import aws_sdk_quicksight.types.table_options

        out["table_options"] = aws_sdk_quicksight.types.table_options.deserialize_json(
            data["TableOptions"]
        )
    if "TotalOptions" in data:
        import aws_sdk_quicksight.types.total_options

        out["total_options"] = aws_sdk_quicksight.types.total_options.deserialize_json(
            data["TotalOptions"]
        )
    if "FieldOptions" in data:
        import aws_sdk_quicksight.types.table_field_options

        out["field_options"] = (
            aws_sdk_quicksight.types.table_field_options.deserialize_json(
                data["FieldOptions"]
            )
        )
    if "PaginatedReportOptions" in data:
        import aws_sdk_quicksight.types.table_paginated_report_options

        out["paginated_report_options"] = (
            aws_sdk_quicksight.types.table_paginated_report_options.deserialize_json(
                data["PaginatedReportOptions"]
            )
        )
    if "TableInlineVisualizations" in data:
        import aws_sdk_quicksight.types.table_inline_visualization_list

        out["table_inline_visualizations"] = (
            aws_sdk_quicksight.types.table_inline_visualization_list.deserialize_json(
                data["TableInlineVisualizations"]
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
