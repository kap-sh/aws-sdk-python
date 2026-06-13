"""Generated from Smithy shape ``com.amazonaws.odb#ListDbServersOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.db_server_list


class ListDbServersOutput(TypedDict):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    db_servers: "aws_sdk_odb.types.db_server_list.DbServerList"
    """<p>The list of database servers along with their properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDbServersOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_odb.types.db_server_list

    out["dbServers"] = aws_sdk_odb.types.db_server_list.serialize_aws_json_1_0(
        value["db_servers"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDbServersOutput:
    out: ListDbServersOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "dbServers" in data:
        import aws_sdk_odb.types.db_server_list

        out["db_servers"] = aws_sdk_odb.types.db_server_list.deserialize_aws_json_1_0(
            data["dbServers"]
        )
    else:
        raise DeserializationError("ListDbServersOutput.db_servers required")
    return out
