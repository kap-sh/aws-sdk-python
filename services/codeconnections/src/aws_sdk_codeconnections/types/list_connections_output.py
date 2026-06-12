"""Generated from Smithy shape ``com.amazonaws.codeconnections#ListConnectionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.connection_list
    import aws_sdk_codeconnections.types.next_token


class ListConnectionsOutput(TypedDict):
    connections: NotRequired[
        "aws_sdk_codeconnections.types.connection_list.ConnectionList"
    ]
    """<p>A list of connections and the details for each connection, such as status, owner, and provider type.</p>"""
    next_token: NotRequired["aws_sdk_codeconnections.types.next_token.NextToken"]
    """<p>A token that can be used in the next <code>ListConnections</code> call. To view all items in the list, continue to call this operation with each subsequent token until no more <code>nextToken</code> values are returned.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListConnectionsOutput) -> dict:
    out: dict = {}
    if "connections" in value:
        import aws_sdk_codeconnections.types.connection_list

        out["Connections"] = (
            aws_sdk_codeconnections.types.connection_list.serialize_aws_json_1_0(
                value["connections"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListConnectionsOutput:
    out: ListConnectionsOutput = {}  # type: ignore[typeddict-item]
    if "Connections" in data:
        import aws_sdk_codeconnections.types.connection_list

        out["connections"] = (
            aws_sdk_codeconnections.types.connection_list.deserialize_aws_json_1_0(
                data["Connections"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
