"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#FieldStats``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.double
    import aws_sdk_cloudsearch_domain.types.long
    import aws_sdk_cloudsearch_domain.types.string


class FieldStats(TypedDict):
    min: NotRequired["aws_sdk_cloudsearch_domain.types.string.String"]
    r"""<p>The minimum value found in the specified field in the result set.</p> <p>If the field is numeric (<code>int</code>, <code>int-array</code>, <code>double</code>, or <code>double-array</code>), <code>min</code> is the string representation of a double-precision 64-bit floating point value. If the field is <code>date</code> or <code>date-array</code>, <code>min</code> is the string representation of a date with the format specified in <a href=\"http://tools.ietf.org/html/rfc3339\">IETF RFC3339</a>: yyyy-mm-ddTHH:mm:ss.SSSZ.</p>"""
    max: NotRequired["aws_sdk_cloudsearch_domain.types.string.String"]
    r"""<p>The maximum value found in the specified field in the result set.</p> <p>If the field is numeric (<code>int</code>, <code>int-array</code>, <code>double</code>, or <code>double-array</code>), <code>max</code> is the string representation of a double-precision 64-bit floating point value. If the field is <code>date</code> or <code>date-array</code>, <code>max</code> is the string representation of a date with the format specified in <a href=\"http://tools.ietf.org/html/rfc3339\">IETF RFC3339</a>: yyyy-mm-ddTHH:mm:ss.SSSZ.</p>"""
    count: "aws_sdk_cloudsearch_domain.types.long.Long"
    """<p>The number of documents that contain a value in the specified field in the result set.</p>"""
    missing: "aws_sdk_cloudsearch_domain.types.long.Long"
    """<p>The number of documents that do not contain a value in the specified field in the result set.</p>"""
    sum: "aws_sdk_cloudsearch_domain.types.double.Double"
    """<p>The sum of the field values across the documents in the result set. <code>null</code> for date fields.</p>"""
    sum_of_squares: "aws_sdk_cloudsearch_domain.types.double.Double"
    """<p>The sum of all field values in the result set squared.</p>"""
    mean: NotRequired["aws_sdk_cloudsearch_domain.types.string.String"]
    r"""<p>The average of the values found in the specified field in the result set.</p> <p>If the field is numeric (<code>int</code>, <code>int-array</code>, <code>double</code>, or <code>double-array</code>), <code>mean</code> is the string representation of a double-precision 64-bit floating point value. If the field is <code>date</code> or <code>date-array</code>, <code>mean</code> is the string representation of a date with the format specified in <a href=\"http://tools.ietf.org/html/rfc3339\">IETF RFC3339</a>: yyyy-mm-ddTHH:mm:ss.SSSZ.</p>"""
    stddev: "aws_sdk_cloudsearch_domain.types.double.Double"
    """<p>The standard deviation of the values in the specified field in the result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldStats) -> dict:
    out: dict = {}
    if "min" in value:
        out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    out["count"] = value.get("count", 0)
    out["missing"] = value.get("missing", 0)
    out["sum"] = value.get("sum", 0)
    out["sumOfSquares"] = value.get("sum_of_squares", 0)
    if "mean" in value:
        out["mean"] = value["mean"]
    out["stddev"] = value.get("stddev", 0)
    return out


def deserialize_json(data: dict) -> FieldStats:
    out: FieldStats = {}  # type: ignore[typeddict-item]
    if "min" in data:
        out["min"] = data["min"]
    if "max" in data:
        out["max"] = data["max"]
    if "count" in data:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    if "missing" in data:
        out["missing"] = data["missing"]
    else:
        out["missing"] = 0
    if "sum" in data:
        out["sum"] = data["sum"]
    else:
        out["sum"] = 0
    if "sumOfSquares" in data:
        out["sum_of_squares"] = data["sumOfSquares"]
    else:
        out["sum_of_squares"] = 0
    if "mean" in data:
        out["mean"] = data["mean"]
    if "stddev" in data:
        out["stddev"] = data["stddev"]
    else:
        out["stddev"] = 0
    return out
