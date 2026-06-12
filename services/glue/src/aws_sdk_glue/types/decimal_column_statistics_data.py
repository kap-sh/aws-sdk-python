"""Generated from Smithy shape ``com.amazonaws.glue#DecimalColumnStatisticsData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.decimal_number
    import aws_sdk_glue.types.non_negative_long


class DecimalColumnStatisticsData(TypedDict):
    minimum_value: NotRequired["aws_sdk_glue.types.decimal_number.DecimalNumber"]
    """<p>The lowest value in the column.</p>"""
    maximum_value: NotRequired["aws_sdk_glue.types.decimal_number.DecimalNumber"]
    """<p>The highest value in the column.</p>"""
    number_of_nulls: "aws_sdk_glue.types.non_negative_long.NonNegativeLong"
    """<p>The number of null values in the column.</p>"""
    number_of_distinct_values: "aws_sdk_glue.types.non_negative_long.NonNegativeLong"
    """<p>The number of distinct values in a column.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DecimalColumnStatisticsData) -> dict:
    out: dict = {}
    if "minimum_value" in value:
        import aws_sdk_glue.types.decimal_number

        out["MinimumValue"] = aws_sdk_glue.types.decimal_number.serialize_aws_json_1_1(
            value["minimum_value"]
        )
    if "maximum_value" in value:
        import aws_sdk_glue.types.decimal_number

        out["MaximumValue"] = aws_sdk_glue.types.decimal_number.serialize_aws_json_1_1(
            value["maximum_value"]
        )
    out["NumberOfNulls"] = value.get("number_of_nulls", 0)
    out["NumberOfDistinctValues"] = value.get("number_of_distinct_values", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DecimalColumnStatisticsData:
    out: DecimalColumnStatisticsData = {}  # type: ignore[typeddict-item]
    if "MinimumValue" in data:
        import aws_sdk_glue.types.decimal_number

        out["minimum_value"] = (
            aws_sdk_glue.types.decimal_number.deserialize_aws_json_1_1(
                data["MinimumValue"]
            )
        )
    if "MaximumValue" in data:
        import aws_sdk_glue.types.decimal_number

        out["maximum_value"] = (
            aws_sdk_glue.types.decimal_number.deserialize_aws_json_1_1(
                data["MaximumValue"]
            )
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
