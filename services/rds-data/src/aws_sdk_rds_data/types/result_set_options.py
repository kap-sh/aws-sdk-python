"""Generated from Smithy shape ``com.amazonaws.rdsdata#ResultSetOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.decimal_return_type
    import aws_sdk_rds_data.types.long_return_type


class ResultSetOptions(TypedDict, closed=True):
    decimal_return_type: NotRequired[
        "aws_sdk_rds_data.types.decimal_return_type.DecimalReturnType"
    ]
    """<p>A value that indicates how a field of <code>DECIMAL</code> type is represented in the response. The value of <code>STRING</code>, the default, specifies that it is converted to a String value. The value of <code>DOUBLE_OR_LONG</code> specifies that it is converted to a Long value if its scale is 0, or to a Double value otherwise.</p> <note> <p>Conversion to Double or Long can result in roundoff errors due to precision loss. We recommend converting to String, especially when working with currency values.</p> </note>"""
    long_return_type: NotRequired[
        "aws_sdk_rds_data.types.long_return_type.LongReturnType"
    ]
    """<p>A value that indicates how a field of <code>LONG</code> type is represented. Allowed values are <code>LONG</code> and <code>STRING</code>. The default is <code>LONG</code>. Specify <code>STRING</code> if the length or precision of numeric values might cause truncation or rounding errors. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResultSetOptions) -> dict:
    out: dict = {}
    if "decimal_return_type" in value:
        import aws_sdk_rds_data.types.decimal_return_type

        out["decimalReturnType"] = (
            aws_sdk_rds_data.types.decimal_return_type.serialize_json(
                value["decimal_return_type"]
            )
        )
    if "long_return_type" in value:
        import aws_sdk_rds_data.types.long_return_type

        out["longReturnType"] = aws_sdk_rds_data.types.long_return_type.serialize_json(
            value["long_return_type"]
        )
    return out


def deserialize_json(data: dict) -> ResultSetOptions:
    out: ResultSetOptions = {}  # type: ignore[typeddict-item]
    if "decimalReturnType" in data:
        import aws_sdk_rds_data.types.decimal_return_type

        out["decimal_return_type"] = (
            aws_sdk_rds_data.types.decimal_return_type.deserialize_json(
                data["decimalReturnType"]
            )
        )
    if "longReturnType" in data:
        import aws_sdk_rds_data.types.long_return_type

        out["long_return_type"] = (
            aws_sdk_rds_data.types.long_return_type.deserialize_json(
                data["longReturnType"]
            )
        )
    return out
