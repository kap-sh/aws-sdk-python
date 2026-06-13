"""Generated from Smithy shape ``com.amazonaws.quicksight#TreeMapConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.chart_axis_label_options
    import aws_sdk_quicksight.types.color_scale
    import aws_sdk_quicksight.types.data_label_options
    import aws_sdk_quicksight.types.legend_options
    import aws_sdk_quicksight.types.tooltip_options
    import aws_sdk_quicksight.types.tree_map_field_wells
    import aws_sdk_quicksight.types.tree_map_sort_configuration
    import aws_sdk_quicksight.types.visual_interaction_options


class TreeMapConfiguration(TypedDict):
    field_wells: NotRequired[
        "aws_sdk_quicksight.types.tree_map_field_wells.TreeMapFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "aws_sdk_quicksight.types.tree_map_sort_configuration.TreeMapSortConfiguration"
    ]
    """<p>The sort configuration of a tree map.</p>"""
    group_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility) of the groups that are displayed in a tree map.</p>"""
    size_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility) of the sizes that are displayed in a tree map.</p>"""
    color_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility) for the colors displayed in a tree map.</p>"""
    color_scale: NotRequired["aws_sdk_quicksight.types.color_scale.ColorScale"]
    """<p>The color options (gradient color, point of divergence) of a tree map.</p>"""
    legend: NotRequired["aws_sdk_quicksight.types.legend_options.LegendOptions"]
    """<p>The legend display setup of the visual.</p>"""
    data_labels: NotRequired[
        "aws_sdk_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The options that determine if visual data labels are displayed.</p>"""
    tooltip: NotRequired["aws_sdk_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The tooltip display setup of the visual.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TreeMapConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import aws_sdk_quicksight.types.tree_map_field_wells

        out["FieldWells"] = (
            aws_sdk_quicksight.types.tree_map_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import aws_sdk_quicksight.types.tree_map_sort_configuration

        out["SortConfiguration"] = (
            aws_sdk_quicksight.types.tree_map_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "group_label_options" in value:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["GroupLabelOptions"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.serialize_json(
                value["group_label_options"]
            )
        )
    if "size_label_options" in value:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["SizeLabelOptions"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.serialize_json(
                value["size_label_options"]
            )
        )
    if "color_label_options" in value:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["ColorLabelOptions"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.serialize_json(
                value["color_label_options"]
            )
        )
    if "color_scale" in value:
        import aws_sdk_quicksight.types.color_scale

        out["ColorScale"] = aws_sdk_quicksight.types.color_scale.serialize_json(
            value["color_scale"]
        )
    if "legend" in value:
        import aws_sdk_quicksight.types.legend_options

        out["Legend"] = aws_sdk_quicksight.types.legend_options.serialize_json(
            value["legend"]
        )
    if "data_labels" in value:
        import aws_sdk_quicksight.types.data_label_options

        out["DataLabels"] = aws_sdk_quicksight.types.data_label_options.serialize_json(
            value["data_labels"]
        )
    if "tooltip" in value:
        import aws_sdk_quicksight.types.tooltip_options

        out["Tooltip"] = aws_sdk_quicksight.types.tooltip_options.serialize_json(
            value["tooltip"]
        )
    if "interactions" in value:
        import aws_sdk_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            aws_sdk_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> TreeMapConfiguration:
    out: TreeMapConfiguration = {}  # type: ignore[typeddict-item]
    if "FieldWells" in data:
        import aws_sdk_quicksight.types.tree_map_field_wells

        out["field_wells"] = (
            aws_sdk_quicksight.types.tree_map_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if "SortConfiguration" in data:
        import aws_sdk_quicksight.types.tree_map_sort_configuration

        out["sort_configuration"] = (
            aws_sdk_quicksight.types.tree_map_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if "GroupLabelOptions" in data:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["group_label_options"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.deserialize_json(
                data["GroupLabelOptions"]
            )
        )
    if "SizeLabelOptions" in data:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["size_label_options"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.deserialize_json(
                data["SizeLabelOptions"]
            )
        )
    if "ColorLabelOptions" in data:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["color_label_options"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.deserialize_json(
                data["ColorLabelOptions"]
            )
        )
    if "ColorScale" in data:
        import aws_sdk_quicksight.types.color_scale

        out["color_scale"] = aws_sdk_quicksight.types.color_scale.deserialize_json(
            data["ColorScale"]
        )
    if "Legend" in data:
        import aws_sdk_quicksight.types.legend_options

        out["legend"] = aws_sdk_quicksight.types.legend_options.deserialize_json(
            data["Legend"]
        )
    if "DataLabels" in data:
        import aws_sdk_quicksight.types.data_label_options

        out["data_labels"] = (
            aws_sdk_quicksight.types.data_label_options.deserialize_json(
                data["DataLabels"]
            )
        )
    if "Tooltip" in data:
        import aws_sdk_quicksight.types.tooltip_options

        out["tooltip"] = aws_sdk_quicksight.types.tooltip_options.deserialize_json(
            data["Tooltip"]
        )
    if "Interactions" in data:
        import aws_sdk_quicksight.types.visual_interaction_options

        out["interactions"] = (
            aws_sdk_quicksight.types.visual_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out
