"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#ListDatabasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.database_list
    import capo_timestream_write.types.string


class ListDatabasesResponse(TypedDict, closed=True):
    databases: NotRequired["capo_timestream_write.types.database_list.DatabaseList"]
    """<p>A list of database names.</p>"""
    next_token: NotRequired["capo_timestream_write.types.string.String"]
    """<p>The pagination token. This parameter is returned when the response is truncated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDatabasesResponse) -> dict:
    out: dict = {}
    if "databases" in value:
        import capo_timestream_write.types.database_list

        out["Databases"] = (
            capo_timestream_write.types.database_list.serialize_aws_json_1_0(
                value["databases"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDatabasesResponse:
    out: ListDatabasesResponse = {}  # type: ignore[typeddict-item]
    if "Databases" in data:
        import capo_timestream_write.types.database_list

        out["databases"] = (
            capo_timestream_write.types.database_list.deserialize_aws_json_1_0(
                data["Databases"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
