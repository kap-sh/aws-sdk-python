"""Generated from Smithy shape ``com.amazonaws.athena#ResultSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.result_set_metadata
    import aws_sdk_athena.types.row_list


class ResultSet(TypedDict, closed=True):
    rows: NotRequired["aws_sdk_athena.types.row_list.RowList"]
    """<p>The rows in the table.</p>"""
    result_set_metadata: NotRequired[
        "aws_sdk_athena.types.result_set_metadata.ResultSetMetadata"
    ]
    """<p>The metadata that describes the column structure and data types of a table of query results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResultSet) -> dict:
    out: dict = {}
    if "rows" in value:
        import aws_sdk_athena.types.row_list

        out["Rows"] = aws_sdk_athena.types.row_list.serialize_aws_json_1_1(
            value["rows"]
        )
    if "result_set_metadata" in value:
        import aws_sdk_athena.types.result_set_metadata

        out["ResultSetMetadata"] = (
            aws_sdk_athena.types.result_set_metadata.serialize_aws_json_1_1(
                value["result_set_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResultSet:
    out: ResultSet = {}  # type: ignore[typeddict-item]
    if "Rows" in data:
        import aws_sdk_athena.types.row_list

        out["rows"] = aws_sdk_athena.types.row_list.deserialize_aws_json_1_1(
            data["Rows"]
        )
    if "ResultSetMetadata" in data:
        import aws_sdk_athena.types.result_set_metadata

        out["result_set_metadata"] = (
            aws_sdk_athena.types.result_set_metadata.deserialize_aws_json_1_1(
                data["ResultSetMetadata"]
            )
        )
    return out
