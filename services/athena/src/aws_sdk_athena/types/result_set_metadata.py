"""Generated from Smithy shape ``com.amazonaws.athena#ResultSetMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.column_info_list


class ResultSetMetadata(TypedDict, closed=True):
    column_info: NotRequired["aws_sdk_athena.types.column_info_list.ColumnInfoList"]
    """<p>Information about the columns returned in a query result metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResultSetMetadata) -> dict:
    out: dict = {}
    if "column_info" in value:
        import aws_sdk_athena.types.column_info_list

        out["ColumnInfo"] = (
            aws_sdk_athena.types.column_info_list.serialize_aws_json_1_1(
                value["column_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResultSetMetadata:
    out: ResultSetMetadata = {}  # type: ignore[typeddict-item]
    if "ColumnInfo" in data:
        import aws_sdk_athena.types.column_info_list

        out["column_info"] = (
            aws_sdk_athena.types.column_info_list.deserialize_aws_json_1_1(
                data["ColumnInfo"]
            )
        )
    return out
