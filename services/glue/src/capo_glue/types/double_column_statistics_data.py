"""Generated from Smithy shape ``com.amazonaws.glue#DoubleColumnStatisticsData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.double
    import capo_glue.types.non_negative_long


class DoubleColumnStatisticsData(TypedDict, closed=True):
    minimum_value: "capo_glue.types.double.Double"
    """<p>The lowest value in the column.</p>"""
    maximum_value: "capo_glue.types.double.Double"
    """<p>The highest value in the column.</p>"""
    number_of_nulls: "capo_glue.types.non_negative_long.NonNegativeLong"
    """<p>The number of null values in the column.</p>"""
    number_of_distinct_values: "capo_glue.types.non_negative_long.NonNegativeLong"
    """<p>The number of distinct values in a column.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DoubleColumnStatisticsData) -> dict:
    out: dict = {}
    out["MinimumValue"] = value.get("minimum_value", 0)
    out["MaximumValue"] = value.get("maximum_value", 0)
    out["NumberOfNulls"] = value.get("number_of_nulls", 0)
    out["NumberOfDistinctValues"] = value.get("number_of_distinct_values", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DoubleColumnStatisticsData:
    out: DoubleColumnStatisticsData = {}  # type: ignore[typeddict-item]
    if "MinimumValue" in data:
        out["minimum_value"] = data["MinimumValue"]
    else:
        out["minimum_value"] = 0
    if "MaximumValue" in data:
        out["maximum_value"] = data["MaximumValue"]
    else:
        out["maximum_value"] = 0
    if "NumberOfNulls" in data:
        out["number_of_nulls"] = data["NumberOfNulls"]
    else:
        out["number_of_nulls"] = 0
    if "NumberOfDistinctValues" in data:
        out["number_of_distinct_values"] = data["NumberOfDistinctValues"]
    else:
        out["number_of_distinct_values"] = 0
    return out
