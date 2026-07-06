"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudChartConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.chart_axis_label_options
    import aws_sdk_quicksight.types.visual_interaction_options
    import aws_sdk_quicksight.types.word_cloud_field_wells
    import aws_sdk_quicksight.types.word_cloud_options
    import aws_sdk_quicksight.types.word_cloud_sort_configuration


class WordCloudChartConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "aws_sdk_quicksight.types.word_cloud_field_wells.WordCloudFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "aws_sdk_quicksight.types.word_cloud_sort_configuration.WordCloudSortConfiguration"
    ]
    """<p>The sort configuration of a word cloud visual.</p>"""
    category_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility, and sort icon visibility) for the word cloud category.</p>"""
    word_cloud_options: NotRequired[
        "aws_sdk_quicksight.types.word_cloud_options.WordCloudOptions"
    ]
    """<p>The options for a word cloud visual.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WordCloudChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import aws_sdk_quicksight.types.word_cloud_field_wells

        out["FieldWells"] = (
            aws_sdk_quicksight.types.word_cloud_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import aws_sdk_quicksight.types.word_cloud_sort_configuration

        out["SortConfiguration"] = (
            aws_sdk_quicksight.types.word_cloud_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "category_label_options" in value:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["CategoryLabelOptions"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.serialize_json(
                value["category_label_options"]
            )
        )
    if "word_cloud_options" in value:
        import aws_sdk_quicksight.types.word_cloud_options

        out["WordCloudOptions"] = (
            aws_sdk_quicksight.types.word_cloud_options.serialize_json(
                value["word_cloud_options"]
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


def deserialize_json(data: dict) -> WordCloudChartConfiguration:
    out: WordCloudChartConfiguration = {}  # type: ignore[typeddict-item]
    if "FieldWells" in data:
        import aws_sdk_quicksight.types.word_cloud_field_wells

        out["field_wells"] = (
            aws_sdk_quicksight.types.word_cloud_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if "SortConfiguration" in data:
        import aws_sdk_quicksight.types.word_cloud_sort_configuration

        out["sort_configuration"] = (
            aws_sdk_quicksight.types.word_cloud_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if "CategoryLabelOptions" in data:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["category_label_options"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.deserialize_json(
                data["CategoryLabelOptions"]
            )
        )
    if "WordCloudOptions" in data:
        import aws_sdk_quicksight.types.word_cloud_options

        out["word_cloud_options"] = (
            aws_sdk_quicksight.types.word_cloud_options.deserialize_json(
                data["WordCloudOptions"]
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
