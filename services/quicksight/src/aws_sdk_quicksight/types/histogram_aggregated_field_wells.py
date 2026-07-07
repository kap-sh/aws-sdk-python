"""Generated from Smithy shape ``com.amazonaws.quicksight#HistogramAggregatedFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.histogram_measure_field_list


class HistogramAggregatedFieldWells(TypedDict, closed=True):
    values: NotRequired[
        "aws_sdk_quicksight.types.histogram_measure_field_list.HistogramMeasureFieldList"
    ]
    """<p>The value field wells of a histogram. Values are aggregated by <code>COUNT</code> or <code>DISTINCT_COUNT</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HistogramAggregatedFieldWells) -> dict:
    out: dict = {}
    if "values" in value:
        import aws_sdk_quicksight.types.histogram_measure_field_list

        out["Values"] = (
            aws_sdk_quicksight.types.histogram_measure_field_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> HistogramAggregatedFieldWells:
    out: HistogramAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "Values" in data:
        import aws_sdk_quicksight.types.histogram_measure_field_list

        out["values"] = (
            aws_sdk_quicksight.types.histogram_measure_field_list.deserialize_json(
                data["Values"]
            )
        )
    return out
