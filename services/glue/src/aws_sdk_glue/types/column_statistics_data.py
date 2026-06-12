"""Generated from Smithy shape ``com.amazonaws.glue#ColumnStatisticsData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.binary_column_statistics_data
    import aws_sdk_glue.types.boolean_column_statistics_data
    import aws_sdk_glue.types.column_statistics_type
    import aws_sdk_glue.types.date_column_statistics_data
    import aws_sdk_glue.types.decimal_column_statistics_data
    import aws_sdk_glue.types.double_column_statistics_data
    import aws_sdk_glue.types.long_column_statistics_data
    import aws_sdk_glue.types.string_column_statistics_data


class ColumnStatisticsData(TypedDict):
    type: "aws_sdk_glue.types.column_statistics_type.ColumnStatisticsType"
    """<p>The type of column statistics data.</p>"""
    boolean_column_statistics_data: NotRequired[
        "aws_sdk_glue.types.boolean_column_statistics_data.BooleanColumnStatisticsData"
    ]
    """<p>Boolean column statistics data.</p>"""
    date_column_statistics_data: NotRequired[
        "aws_sdk_glue.types.date_column_statistics_data.DateColumnStatisticsData"
    ]
    """<p>Date column statistics data.</p>"""
    decimal_column_statistics_data: NotRequired[
        "aws_sdk_glue.types.decimal_column_statistics_data.DecimalColumnStatisticsData"
    ]
    """<p> Decimal column statistics data. UnscaledValues within are Base64-encoded binary objects storing big-endian, two's complement representations of the decimal's unscaled value. </p>"""
    double_column_statistics_data: NotRequired[
        "aws_sdk_glue.types.double_column_statistics_data.DoubleColumnStatisticsData"
    ]
    """<p>Double column statistics data.</p>"""
    long_column_statistics_data: NotRequired[
        "aws_sdk_glue.types.long_column_statistics_data.LongColumnStatisticsData"
    ]
    """<p>Long column statistics data.</p>"""
    string_column_statistics_data: NotRequired[
        "aws_sdk_glue.types.string_column_statistics_data.StringColumnStatisticsData"
    ]
    """<p>String column statistics data.</p>"""
    binary_column_statistics_data: NotRequired[
        "aws_sdk_glue.types.binary_column_statistics_data.BinaryColumnStatisticsData"
    ]
    """<p>Binary column statistics data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnStatisticsData) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.column_statistics_type

    out["Type"] = aws_sdk_glue.types.column_statistics_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "boolean_column_statistics_data" in value:
        import aws_sdk_glue.types.boolean_column_statistics_data

        out["BooleanColumnStatisticsData"] = (
            aws_sdk_glue.types.boolean_column_statistics_data.serialize_aws_json_1_1(
                value["boolean_column_statistics_data"]
            )
        )
    if "date_column_statistics_data" in value:
        import aws_sdk_glue.types.date_column_statistics_data

        out["DateColumnStatisticsData"] = (
            aws_sdk_glue.types.date_column_statistics_data.serialize_aws_json_1_1(
                value["date_column_statistics_data"]
            )
        )
    if "decimal_column_statistics_data" in value:
        import aws_sdk_glue.types.decimal_column_statistics_data

        out["DecimalColumnStatisticsData"] = (
            aws_sdk_glue.types.decimal_column_statistics_data.serialize_aws_json_1_1(
                value["decimal_column_statistics_data"]
            )
        )
    if "double_column_statistics_data" in value:
        import aws_sdk_glue.types.double_column_statistics_data

        out["DoubleColumnStatisticsData"] = (
            aws_sdk_glue.types.double_column_statistics_data.serialize_aws_json_1_1(
                value["double_column_statistics_data"]
            )
        )
    if "long_column_statistics_data" in value:
        import aws_sdk_glue.types.long_column_statistics_data

        out["LongColumnStatisticsData"] = (
            aws_sdk_glue.types.long_column_statistics_data.serialize_aws_json_1_1(
                value["long_column_statistics_data"]
            )
        )
    if "string_column_statistics_data" in value:
        import aws_sdk_glue.types.string_column_statistics_data

        out["StringColumnStatisticsData"] = (
            aws_sdk_glue.types.string_column_statistics_data.serialize_aws_json_1_1(
                value["string_column_statistics_data"]
            )
        )
    if "binary_column_statistics_data" in value:
        import aws_sdk_glue.types.binary_column_statistics_data

        out["BinaryColumnStatisticsData"] = (
            aws_sdk_glue.types.binary_column_statistics_data.serialize_aws_json_1_1(
                value["binary_column_statistics_data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ColumnStatisticsData:
    out: ColumnStatisticsData = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_glue.types.column_statistics_type

        out["type"] = (
            aws_sdk_glue.types.column_statistics_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("ColumnStatisticsData.type required")
    if "BooleanColumnStatisticsData" in data:
        import aws_sdk_glue.types.boolean_column_statistics_data

        out["boolean_column_statistics_data"] = (
            aws_sdk_glue.types.boolean_column_statistics_data.deserialize_aws_json_1_1(
                data["BooleanColumnStatisticsData"]
            )
        )
    if "DateColumnStatisticsData" in data:
        import aws_sdk_glue.types.date_column_statistics_data

        out["date_column_statistics_data"] = (
            aws_sdk_glue.types.date_column_statistics_data.deserialize_aws_json_1_1(
                data["DateColumnStatisticsData"]
            )
        )
    if "DecimalColumnStatisticsData" in data:
        import aws_sdk_glue.types.decimal_column_statistics_data

        out["decimal_column_statistics_data"] = (
            aws_sdk_glue.types.decimal_column_statistics_data.deserialize_aws_json_1_1(
                data["DecimalColumnStatisticsData"]
            )
        )
    if "DoubleColumnStatisticsData" in data:
        import aws_sdk_glue.types.double_column_statistics_data

        out["double_column_statistics_data"] = (
            aws_sdk_glue.types.double_column_statistics_data.deserialize_aws_json_1_1(
                data["DoubleColumnStatisticsData"]
            )
        )
    if "LongColumnStatisticsData" in data:
        import aws_sdk_glue.types.long_column_statistics_data

        out["long_column_statistics_data"] = (
            aws_sdk_glue.types.long_column_statistics_data.deserialize_aws_json_1_1(
                data["LongColumnStatisticsData"]
            )
        )
    if "StringColumnStatisticsData" in data:
        import aws_sdk_glue.types.string_column_statistics_data

        out["string_column_statistics_data"] = (
            aws_sdk_glue.types.string_column_statistics_data.deserialize_aws_json_1_1(
                data["StringColumnStatisticsData"]
            )
        )
    if "BinaryColumnStatisticsData" in data:
        import aws_sdk_glue.types.binary_column_statistics_data

        out["binary_column_statistics_data"] = (
            aws_sdk_glue.types.binary_column_statistics_data.deserialize_aws_json_1_1(
                data["BinaryColumnStatisticsData"]
            )
        )
    return out
