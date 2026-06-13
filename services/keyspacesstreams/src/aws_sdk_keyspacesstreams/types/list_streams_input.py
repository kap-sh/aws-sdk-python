"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#ListStreamsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.keyspace_name
    import aws_sdk_keyspacesstreams.types.stream_arn_token
    import aws_sdk_keyspacesstreams.types.table_name


class ListStreamsInput(TypedDict):
    keyspace_name: NotRequired[
        "aws_sdk_keyspacesstreams.types.keyspace_name.KeyspaceName"
    ]
    """<p> The name of the keyspace for which to list streams. If specified, only streams associated with tables in this keyspace are returned. If omitted, streams from all keyspaces are included in the results. </p>"""
    table_name: NotRequired["aws_sdk_keyspacesstreams.types.table_name.TableName"]
    """<p> The name of the table for which to list streams. Must be used together with <code>keyspaceName</code>. If specified, only streams associated with this specific table are returned. </p>"""
    max_results: NotRequired["int"]
    """<p> The maximum number of streams to return in a single <code>ListStreams</code> request. The default value is 100. The minimum value is 1 and the maximum value is 100. </p>"""
    next_token: NotRequired[
        "aws_sdk_keyspacesstreams.types.stream_arn_token.StreamArnToken"
    ]
    """<p> An optional pagination token provided by a previous <code>ListStreams</code> operation. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>maxResults</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListStreamsInput) -> dict:
    out: dict = {}
    if "keyspace_name" in value:
        out["keyspaceName"] = value["keyspace_name"]
    if "table_name" in value:
        out["tableName"] = value["table_name"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListStreamsInput:
    out: ListStreamsInput = {}  # type: ignore[typeddict-item]
    if "keyspaceName" in data:
        out["keyspace_name"] = data["keyspaceName"]
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
