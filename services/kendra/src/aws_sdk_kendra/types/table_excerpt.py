"""Generated from Smithy shape ``com.amazonaws.kendra#TableExcerpt``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.integer
    import aws_sdk_kendra.types.table_row_list


class TableExcerpt(TypedDict, closed=True):
    rows: NotRequired["aws_sdk_kendra.types.table_row_list.TableRowList"]
    """<p>A list of rows in the table excerpt.</p>"""
    total_number_of_rows: NotRequired["aws_sdk_kendra.types.integer.Integer"]
    """<p>A count of the number of rows in the original table within the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableExcerpt) -> dict:
    out: dict = {}
    if "rows" in value:
        import aws_sdk_kendra.types.table_row_list

        out["Rows"] = aws_sdk_kendra.types.table_row_list.serialize_aws_json_1_1(
            value["rows"]
        )
    if "total_number_of_rows" in value:
        out["TotalNumberOfRows"] = value["total_number_of_rows"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TableExcerpt:
    out: TableExcerpt = {}  # type: ignore[typeddict-item]
    if "Rows" in data:
        import aws_sdk_kendra.types.table_row_list

        out["rows"] = aws_sdk_kendra.types.table_row_list.deserialize_aws_json_1_1(
            data["Rows"]
        )
    if "TotalNumberOfRows" in data:
        out["total_number_of_rows"] = data["TotalNumberOfRows"]
    return out
