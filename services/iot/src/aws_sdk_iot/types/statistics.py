"""Generated from Smithy shape ``com.amazonaws.iot#Statistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.average
    import aws_sdk_iot.types.count
    import aws_sdk_iot.types.maximum
    import aws_sdk_iot.types.minimum
    import aws_sdk_iot.types.std_deviation
    import aws_sdk_iot.types.sum
    import aws_sdk_iot.types.sum_of_squares
    import aws_sdk_iot.types.variance


class Statistics(TypedDict):
    count: "aws_sdk_iot.types.count.Count"
    """<p>The count of things that match the query string criteria and contain a valid aggregation field value.</p>"""
    average: NotRequired["aws_sdk_iot.types.average.Average"]
    """<p>The average of the aggregated field values.</p>"""
    sum: NotRequired["aws_sdk_iot.types.sum.Sum"]
    """<p>The sum of the aggregated field values.</p>"""
    minimum: NotRequired["aws_sdk_iot.types.minimum.Minimum"]
    """<p>The minimum aggregated field value.</p>"""
    maximum: NotRequired["aws_sdk_iot.types.maximum.Maximum"]
    """<p>The maximum aggregated field value.</p>"""
    sum_of_squares: NotRequired["aws_sdk_iot.types.sum_of_squares.SumOfSquares"]
    """<p>The sum of the squares of the aggregated field values.</p>"""
    variance: NotRequired["aws_sdk_iot.types.variance.Variance"]
    """<p>The variance of the aggregated field values.</p>"""
    std_deviation: NotRequired["aws_sdk_iot.types.std_deviation.StdDeviation"]
    """<p>The standard deviation of the aggregated field values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Statistics) -> dict:
    out: dict = {}
    out["count"] = value.get("count", 0)
    if "average" in value:
        out["average"] = value["average"]
    if "sum" in value:
        out["sum"] = value["sum"]
    if "minimum" in value:
        out["minimum"] = value["minimum"]
    if "maximum" in value:
        out["maximum"] = value["maximum"]
    if "sum_of_squares" in value:
        out["sumOfSquares"] = value["sum_of_squares"]
    if "variance" in value:
        out["variance"] = value["variance"]
    if "std_deviation" in value:
        out["stdDeviation"] = value["std_deviation"]
    return out


def deserialize_json(data: dict) -> Statistics:
    out: Statistics = {}  # type: ignore[typeddict-item]
    if "count" in data:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    if "average" in data:
        out["average"] = data["average"]
    if "sum" in data:
        out["sum"] = data["sum"]
    if "minimum" in data:
        out["minimum"] = data["minimum"]
    if "maximum" in data:
        out["maximum"] = data["maximum"]
    if "sumOfSquares" in data:
        out["sum_of_squares"] = data["sumOfSquares"]
    if "variance" in data:
        out["variance"] = data["variance"]
    if "stdDeviation" in data:
        out["std_deviation"] = data["stdDeviation"]
    return out
