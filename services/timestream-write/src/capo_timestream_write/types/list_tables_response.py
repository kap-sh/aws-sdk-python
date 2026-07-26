"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#ListTablesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.string
    import capo_timestream_write.types.table_list


class ListTablesResponse(TypedDict, closed=True):
    tables: NotRequired["capo_timestream_write.types.table_list.TableList"]
    """<p>A list of tables.</p>"""
    next_token: NotRequired["capo_timestream_write.types.string.String"]
    """<p>A token to specify where to start paginating. This is the NextToken from a previously truncated response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTablesResponse) -> dict:
    out: dict = {}
    if "tables" in value:
        import capo_timestream_write.types.table_list

        out["Tables"] = capo_timestream_write.types.table_list.serialize_aws_json_1_0(
            value["tables"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTablesResponse:
    out: ListTablesResponse = {}  # type: ignore[typeddict-item]
    if "Tables" in data:
        import capo_timestream_write.types.table_list

        out["tables"] = capo_timestream_write.types.table_list.deserialize_aws_json_1_0(
            data["Tables"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
