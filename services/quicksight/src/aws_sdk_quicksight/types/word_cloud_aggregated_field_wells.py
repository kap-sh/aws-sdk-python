"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudAggregatedFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.word_cloud_dimension_field_list
    import aws_sdk_quicksight.types.word_cloud_measure_field_list


class WordCloudAggregatedFieldWells(TypedDict, closed=True):
    group_by: NotRequired[
        "aws_sdk_quicksight.types.word_cloud_dimension_field_list.WordCloudDimensionFieldList"
    ]
    """<p>The group by field well of a word cloud. Values are grouped by group by fields.</p>"""
    size: NotRequired[
        "aws_sdk_quicksight.types.word_cloud_measure_field_list.WordCloudMeasureFieldList"
    ]
    """<p>The size field well of a word cloud. Values are aggregated based on group by fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WordCloudAggregatedFieldWells) -> dict:
    out: dict = {}
    if "group_by" in value:
        import aws_sdk_quicksight.types.word_cloud_dimension_field_list

        out["GroupBy"] = (
            aws_sdk_quicksight.types.word_cloud_dimension_field_list.serialize_json(
                value["group_by"]
            )
        )
    if "size" in value:
        import aws_sdk_quicksight.types.word_cloud_measure_field_list

        out["Size"] = (
            aws_sdk_quicksight.types.word_cloud_measure_field_list.serialize_json(
                value["size"]
            )
        )
    return out


def deserialize_json(data: dict) -> WordCloudAggregatedFieldWells:
    out: WordCloudAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "GroupBy" in data:
        import aws_sdk_quicksight.types.word_cloud_dimension_field_list

        out["group_by"] = (
            aws_sdk_quicksight.types.word_cloud_dimension_field_list.deserialize_json(
                data["GroupBy"]
            )
        )
    if "Size" in data:
        import aws_sdk_quicksight.types.word_cloud_measure_field_list

        out["size"] = (
            aws_sdk_quicksight.types.word_cloud_measure_field_list.deserialize_json(
                data["Size"]
            )
        )
    return out
