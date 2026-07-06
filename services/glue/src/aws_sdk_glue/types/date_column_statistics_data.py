"""Generated from Smithy shape ``com.amazonaws.glue#DateColumnStatisticsData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.non_negative_long
    import aws_sdk_glue.types.timestamp


class DateColumnStatisticsData(TypedDict, closed=True):
    minimum_value: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The lowest value in the column.</p>"""
    maximum_value: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The highest value in the column.</p>"""
    number_of_nulls: "aws_sdk_glue.types.non_negative_long.NonNegativeLong"
    """<p>The number of null values in the column.</p>"""
    number_of_distinct_values: "aws_sdk_glue.types.non_negative_long.NonNegativeLong"
    """<p>The number of distinct values in a column.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DateColumnStatisticsData) -> dict:
    out: dict = {}
    if "minimum_value" in value:
        import aws_sdk_glue.types.timestamp

        out["MinimumValue"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["minimum_value"]
        )
    if "maximum_value" in value:
        import aws_sdk_glue.types.timestamp

        out["MaximumValue"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["maximum_value"]
        )
    out["NumberOfNulls"] = value.get("number_of_nulls", 0)
    out["NumberOfDistinctValues"] = value.get("number_of_distinct_values", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DateColumnStatisticsData:
    out: DateColumnStatisticsData = {}  # type: ignore[typeddict-item]
    if "MinimumValue" in data:
        import aws_sdk_glue.types.timestamp

        out["minimum_value"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["MinimumValue"]
        )
    if "MaximumValue" in data:
        import aws_sdk_glue.types.timestamp

        out["maximum_value"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["MaximumValue"]
        )
    if "NumberOfNulls" in data:
        out["number_of_nulls"] = data["NumberOfNulls"]
    else:
        out["number_of_nulls"] = 0
    if "NumberOfDistinctValues" in data:
        out["number_of_distinct_values"] = data["NumberOfDistinctValues"]
    else:
        out["number_of_distinct_values"] = 0
    return out
