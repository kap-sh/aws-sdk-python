"""Generated from Smithy shape ``com.amazonaws.glue#BinaryColumnStatisticsData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.non_negative_double
    import capo_glue.types.non_negative_long


class BinaryColumnStatisticsData(TypedDict, closed=True):
    maximum_length: "capo_glue.types.non_negative_long.NonNegativeLong"
    """<p>The size of the longest bit sequence in the column.</p>"""
    average_length: "capo_glue.types.non_negative_double.NonNegativeDouble"
    """<p>The average bit sequence length in the column.</p>"""
    number_of_nulls: "capo_glue.types.non_negative_long.NonNegativeLong"
    """<p>The number of null values in the column.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BinaryColumnStatisticsData) -> dict:
    out: dict = {}
    out["MaximumLength"] = value.get("maximum_length", 0)
    out["AverageLength"] = value.get("average_length", 0)
    out["NumberOfNulls"] = value.get("number_of_nulls", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> BinaryColumnStatisticsData:
    out: BinaryColumnStatisticsData = {}  # type: ignore[typeddict-item]
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
    return out
