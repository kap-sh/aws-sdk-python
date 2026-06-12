"""Generated from Smithy shape ``com.amazonaws.timestreamquery#Datum``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.datum_list
    import aws_sdk_timestream_query.types.nullable_boolean
    import aws_sdk_timestream_query.types.row
    import aws_sdk_timestream_query.types.scalar_value
    import aws_sdk_timestream_query.types.time_series_data_point_list


class Datum(TypedDict):
    scalar_value: NotRequired["aws_sdk_timestream_query.types.scalar_value.ScalarValue"]
    """<p> Indicates if the data point is a scalar value such as integer, string, double, or Boolean. </p>"""
    time_series_value: NotRequired[
        "aws_sdk_timestream_query.types.time_series_data_point_list.TimeSeriesDataPointList"
    ]
    """<p> Indicates if the data point is a timeseries data type. </p>"""
    array_value: NotRequired["aws_sdk_timestream_query.types.datum_list.DatumList"]
    """<p> Indicates if the data point is an array. </p>"""
    row_value: NotRequired["aws_sdk_timestream_query.types.row.Row"]
    """<p> Indicates if the data point is a row. </p>"""
    null_value: NotRequired[
        "aws_sdk_timestream_query.types.nullable_boolean.NullableBoolean"
    ]
    """<p> Indicates if the data point is null. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Datum) -> dict:
    out: dict = {}
    if "scalar_value" in value:
        out["ScalarValue"] = value["scalar_value"]
    if "time_series_value" in value:
        import aws_sdk_timestream_query.types.time_series_data_point_list

        out["TimeSeriesValue"] = (
            aws_sdk_timestream_query.types.time_series_data_point_list.serialize_aws_json_1_0(
                value["time_series_value"]
            )
        )
    if "array_value" in value:
        import aws_sdk_timestream_query.types.datum_list

        out["ArrayValue"] = (
            aws_sdk_timestream_query.types.datum_list.serialize_aws_json_1_0(
                value["array_value"]
            )
        )
    if "row_value" in value:
        import aws_sdk_timestream_query.types.row

        out["RowValue"] = aws_sdk_timestream_query.types.row.serialize_aws_json_1_0(
            value["row_value"]
        )
    if "null_value" in value:
        out["NullValue"] = value["null_value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Datum:
    out: Datum = {}  # type: ignore[typeddict-item]
    if "ScalarValue" in data:
        out["scalar_value"] = data["ScalarValue"]
    if "TimeSeriesValue" in data:
        import aws_sdk_timestream_query.types.time_series_data_point_list

        out["time_series_value"] = (
            aws_sdk_timestream_query.types.time_series_data_point_list.deserialize_aws_json_1_0(
                data["TimeSeriesValue"]
            )
        )
    if "ArrayValue" in data:
        import aws_sdk_timestream_query.types.datum_list

        out["array_value"] = (
            aws_sdk_timestream_query.types.datum_list.deserialize_aws_json_1_0(
                data["ArrayValue"]
            )
        )
    if "RowValue" in data:
        import aws_sdk_timestream_query.types.row

        out["row_value"] = aws_sdk_timestream_query.types.row.deserialize_aws_json_1_0(
            data["RowValue"]
        )
    if "NullValue" in data:
        out["null_value"] = data["NullValue"]
    return out
