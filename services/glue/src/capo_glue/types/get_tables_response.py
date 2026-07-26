"""Generated from Smithy shape ``com.amazonaws.glue#GetTablesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.table_list
    import capo_glue.types.token


class GetTablesResponse(TypedDict, closed=True):
    table_list: NotRequired["capo_glue.types.table_list.TableList"]
    """<p>A list of the requested <code>Table</code> objects.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, present if the current list segment is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTablesResponse) -> dict:
    out: dict = {}
    if "table_list" in value:
        import capo_glue.types.table_list

        out["TableList"] = capo_glue.types.table_list.serialize_aws_json_1_1(
            value["table_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTablesResponse:
    out: GetTablesResponse = {}  # type: ignore[typeddict-item]
    if "TableList" in data:
        import capo_glue.types.table_list

        out["table_list"] = capo_glue.types.table_list.deserialize_aws_json_1_1(
            data["TableList"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
