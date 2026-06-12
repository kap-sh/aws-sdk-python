"""Generated from Smithy shape ``com.amazonaws.glue#SearchTablesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.table_list
    import aws_sdk_glue.types.token


class SearchTablesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token, present if the current list segment is not the last.</p>"""
    table_list: NotRequired["aws_sdk_glue.types.table_list.TableList"]
    """<p>A list of the requested <code>Table</code> objects. The <code>SearchTables</code> response returns only the tables that you have access to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchTablesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "table_list" in value:
        import aws_sdk_glue.types.table_list

        out["TableList"] = aws_sdk_glue.types.table_list.serialize_aws_json_1_1(
            value["table_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchTablesResponse:
    out: SearchTablesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "TableList" in data:
        import aws_sdk_glue.types.table_list

        out["table_list"] = aws_sdk_glue.types.table_list.deserialize_aws_json_1_1(
            data["TableList"]
        )
    return out
