"""Generated from Smithy shape ``com.amazonaws.quicksight#HistogramFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.histogram_aggregated_field_wells


class HistogramFieldWells(TypedDict):
    histogram_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.histogram_aggregated_field_wells.HistogramAggregatedFieldWells"
    ]
    """<p>The field well configuration of a histogram.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HistogramFieldWells) -> dict:
    out: dict = {}
    if "histogram_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.histogram_aggregated_field_wells

        out["HistogramAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.histogram_aggregated_field_wells.serialize_json(
                value["histogram_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> HistogramFieldWells:
    out: HistogramFieldWells = {}  # type: ignore[typeddict-item]
    if "HistogramAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.histogram_aggregated_field_wells

        out["histogram_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.histogram_aggregated_field_wells.deserialize_json(
                data["HistogramAggregatedFieldWells"]
            )
        )
    return out
