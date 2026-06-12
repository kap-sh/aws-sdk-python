"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ColumnInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.string
    import aws_sdk_timestream_query.types.type


class ColumnInfo(TypedDict):
    name: NotRequired["aws_sdk_timestream_query.types.string.String"]
    """<p> The name of the result set column. The name of the result set is available for columns of all data types except for arrays. </p>"""
    type: "aws_sdk_timestream_query.types.type.Type"
    """<p>The data type of the result set column. The data type can be a scalar or complex. Scalar data types are integers, strings, doubles, Booleans, and others. Complex data types are types such as arrays, rows, and others. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ColumnInfo) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    import aws_sdk_timestream_query.types.type

    out["Type"] = aws_sdk_timestream_query.types.type.serialize_aws_json_1_0(
        value["type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ColumnInfo:
    out: ColumnInfo = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_timestream_query.types.type

        out["type"] = aws_sdk_timestream_query.types.type.deserialize_aws_json_1_0(
            data["Type"]
        )
    else:
        raise DeserializationError("ColumnInfo.type required")
    return out
