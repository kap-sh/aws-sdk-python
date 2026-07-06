"""Generated from Smithy shape ``com.amazonaws.glue#BooleanColumnStatisticsData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.non_negative_long


class BooleanColumnStatisticsData(TypedDict, closed=True):
    number_of_trues: "aws_sdk_glue.types.non_negative_long.NonNegativeLong"
    """<p>The number of true values in the column.</p>"""
    number_of_falses: "aws_sdk_glue.types.non_negative_long.NonNegativeLong"
    """<p>The number of false values in the column.</p>"""
    number_of_nulls: "aws_sdk_glue.types.non_negative_long.NonNegativeLong"
    """<p>The number of null values in the column.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BooleanColumnStatisticsData) -> dict:
    out: dict = {}
    out["NumberOfTrues"] = value.get("number_of_trues", 0)
    out["NumberOfFalses"] = value.get("number_of_falses", 0)
    out["NumberOfNulls"] = value.get("number_of_nulls", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> BooleanColumnStatisticsData:
    out: BooleanColumnStatisticsData = {}  # type: ignore[typeddict-item]
    if "NumberOfTrues" in data:
        out["number_of_trues"] = data["NumberOfTrues"]
    else:
        out["number_of_trues"] = 0
    if "NumberOfFalses" in data:
        out["number_of_falses"] = data["NumberOfFalses"]
    else:
        out["number_of_falses"] = 0
    if "NumberOfNulls" in data:
        out["number_of_nulls"] = data["NumberOfNulls"]
    else:
        out["number_of_nulls"] = 0
    return out
