"""Generated from Smithy shape ``com.amazonaws.directconnect#Connections``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.connection_list
    import aws_sdk_direct_connect.types.pagination_token


class Connections(TypedDict):
    connections: NotRequired[
        "aws_sdk_direct_connect.types.connection_list.ConnectionList"
    ]
    """<p>The connections.</p>"""
    next_token: NotRequired[
        "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Connections) -> dict:
    out: dict = {}
    if "connections" in value:
        import aws_sdk_direct_connect.types.connection_list

        out["connections"] = (
            aws_sdk_direct_connect.types.connection_list.serialize_aws_json_1_1(
                value["connections"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Connections:
    out: Connections = {}  # type: ignore[typeddict-item]
    if "connections" in data:
        import aws_sdk_direct_connect.types.connection_list

        out["connections"] = (
            aws_sdk_direct_connect.types.connection_list.deserialize_aws_json_1_1(
                data["connections"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
