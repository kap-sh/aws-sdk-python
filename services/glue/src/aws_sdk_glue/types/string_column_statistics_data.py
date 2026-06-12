"""Generated from Smithy shape ``com.amazonaws.glue#StringColumnStatisticsData``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.non_negative_double
    import aws_sdk_glue.types.non_negative_long


class StringColumnStatisticsData(TypedDict):
    maximum_length: "aws_sdk_glue.types.non_negative_long.NonNegativeLong"
    """<p>The size of the longest string in the column.</p>"""
    average_length: "aws_sdk_glue.types.non_negative_double.NonNegativeDouble"
    """<p>The average string length in the column.</p>"""
    number_of_nulls: "aws_sdk_glue.types.non_negative_long.NonNegativeLong"
    """<p>The number of null values in the column.</p>"""
    number_of_distinct_values: "aws_sdk_glue.types.non_negative_long.NonNegativeLong"
    """<p>The number of distinct values in a column.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StringColumnStatisticsData) -> dict:
    out: dict = {}
    out["MaximumLength"] = value.get("maximum_length", 0)
    out["AverageLength"] = value.get("average_length", 0)
    out["NumberOfNulls"] = value.get("number_of_nulls", 0)
    out["NumberOfDistinctValues"] = value.get("number_of_distinct_values", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> StringColumnStatisticsData:
    out: StringColumnStatisticsData = {}  # type: ignore[typeddict-item]
    if "MaximumLength" in data:
        out["maximum_length"] = data["MaximumLength"]
    else:
        out["maximum_length"] = 0
    if "AverageLength" in data:
        out["average_length"] = data["AverageLength"]
    else:
        out["average_length"] = 0
    if "NumberOfNulls" in data:
        out["number_of_nulls"] = data["NumberOfNulls"]
    else:
        out["number_of_nulls"] = 0
    if "NumberOfDistinctValues" in data:
        out["number_of_distinct_values"] = data["NumberOfDistinctValues"]
    else:
        out["number_of_distinct_values"] = 0
    return out
