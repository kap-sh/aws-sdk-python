"""Generated from Smithy shape ``com.amazonaws.forecast#Statistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.double
    import aws_sdk_forecast.types.integer
    import aws_sdk_forecast.types.long
    import aws_sdk_forecast.types.string


class Statistics(TypedDict, closed=True):
    count: NotRequired["aws_sdk_forecast.types.integer.Integer"]
    """<p>The number of values in the field. If the response value is -1, refer to <code>CountLong</code>.</p>"""
    count_distinct: NotRequired["aws_sdk_forecast.types.integer.Integer"]
    """<p>The number of distinct values in the field. If the response value is -1, refer to <code>CountDistinctLong</code>.</p>"""
    count_null: NotRequired["aws_sdk_forecast.types.integer.Integer"]
    """<p>The number of null values in the field. If the response value is -1, refer to <code>CountNullLong</code>.</p>"""
    count_nan: NotRequired["aws_sdk_forecast.types.integer.Integer"]
    """<p>The number of NAN (not a number) values in the field. If the response value is -1, refer to <code>CountNanLong</code>.</p>"""
    min: NotRequired["aws_sdk_forecast.types.string.String"]
    """<p>For a numeric field, the minimum value in the field.</p>"""
    max: NotRequired["aws_sdk_forecast.types.string.String"]
    """<p>For a numeric field, the maximum value in the field.</p>"""
    avg: NotRequired["aws_sdk_forecast.types.double.Double"]
    """<p>For a numeric field, the average value in the field.</p>"""
    stddev: NotRequired["aws_sdk_forecast.types.double.Double"]
    """<p>For a numeric field, the standard deviation.</p>"""
    count_long: NotRequired["aws_sdk_forecast.types.long.Long"]
    """<p>The number of values in the field. <code>CountLong</code> is used instead of <code>Count</code> if the value is greater than 2,147,483,647.</p>"""
    count_distinct_long: NotRequired["aws_sdk_forecast.types.long.Long"]
    """<p>The number of distinct values in the field. <code>CountDistinctLong</code> is used instead of <code>CountDistinct</code> if the value is greater than 2,147,483,647.</p>"""
    count_null_long: NotRequired["aws_sdk_forecast.types.long.Long"]
    """<p>The number of null values in the field. <code>CountNullLong</code> is used instead of <code>CountNull</code> if the value is greater than 2,147,483,647.</p>"""
    count_nan_long: NotRequired["aws_sdk_forecast.types.long.Long"]
    """<p>The number of NAN (not a number) values in the field. <code>CountNanLong</code> is used instead of <code>CountNan</code> if the value is greater than 2,147,483,647.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Statistics) -> dict:
    out: dict = {}
    if "count" in value:
        out["Count"] = value["count"]
    if "count_distinct" in value:
        out["CountDistinct"] = value["count_distinct"]
    if "count_null" in value:
        out["CountNull"] = value["count_null"]
    if "count_nan" in value:
        out["CountNan"] = value["count_nan"]
    if "min" in value:
        out["Min"] = value["min"]
    if "max" in value:
        out["Max"] = value["max"]
    if "avg" in value:
        out["Avg"] = value["avg"]
    if "stddev" in value:
        out["Stddev"] = value["stddev"]
    if "count_long" in value:
        out["CountLong"] = value["count_long"]
    if "count_distinct_long" in value:
        out["CountDistinctLong"] = value["count_distinct_long"]
    if "count_null_long" in value:
        out["CountNullLong"] = value["count_null_long"]
    if "count_nan_long" in value:
        out["CountNanLong"] = value["count_nan_long"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Statistics:
    out: Statistics = {}  # type: ignore[typeddict-item]
    if "Count" in data:
        out["count"] = data["Count"]
    if "CountDistinct" in data:
        out["count_distinct"] = data["CountDistinct"]
    if "CountNull" in data:
        out["count_null"] = data["CountNull"]
    if "CountNan" in data:
        out["count_nan"] = data["CountNan"]
    if "Min" in data:
        out["min"] = data["Min"]
    if "Max" in data:
        out["max"] = data["Max"]
    if "Avg" in data:
        out["avg"] = data["Avg"]
    if "Stddev" in data:
        out["stddev"] = data["Stddev"]
    if "CountLong" in data:
        out["count_long"] = data["CountLong"]
    if "CountDistinctLong" in data:
        out["count_distinct_long"] = data["CountDistinctLong"]
    if "CountNullLong" in data:
        out["count_null_long"] = data["CountNullLong"]
    if "CountNanLong" in data:
        out["count_nan_long"] = data["CountNanLong"]
    return out
