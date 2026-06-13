"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.word_cloud_aggregated_field_wells


class WordCloudFieldWells(TypedDict):
    word_cloud_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.word_cloud_aggregated_field_wells.WordCloudAggregatedFieldWells"
    ]
    """<p>The aggregated field wells of a word cloud.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WordCloudFieldWells) -> dict:
    out: dict = {}
    if "word_cloud_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.word_cloud_aggregated_field_wells

        out["WordCloudAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.word_cloud_aggregated_field_wells.serialize_json(
                value["word_cloud_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> WordCloudFieldWells:
    out: WordCloudFieldWells = {}  # type: ignore[typeddict-item]
    if "WordCloudAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.word_cloud_aggregated_field_wells

        out["word_cloud_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.word_cloud_aggregated_field_wells.deserialize_json(
                data["WordCloudAggregatedFieldWells"]
            )
        )
    return out
