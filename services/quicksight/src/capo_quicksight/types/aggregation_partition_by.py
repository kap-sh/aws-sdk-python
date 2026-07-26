"""Generated from Smithy shape ``com.amazonaws.quicksight#AggregationPartitionBy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.limited_string
    import capo_quicksight.types.time_granularity


class AggregationPartitionBy(TypedDict, closed=True):
    field_name: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>The field Name for an <code>AggregationPartitionBy</code>.</p>"""
    time_granularity: NotRequired[
        "capo_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The <code>TimeGranularity</code> for an <code>AggregationPartitionBy</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationPartitionBy) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    if "time_granularity" in value:
        import capo_quicksight.types.time_granularity

        out["TimeGranularity"] = capo_quicksight.types.time_granularity.serialize_json(
            value["time_granularity"]
        )
    return out


def deserialize_json(data: dict) -> AggregationPartitionBy:
    out: AggregationPartitionBy = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        out["field_name"] = data["FieldName"]
    if "TimeGranularity" in data:
        import capo_quicksight.types.time_granularity

        out["time_granularity"] = (
            capo_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    return out
