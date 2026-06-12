"""Generated from Smithy shape ``com.amazonaws.transfer#ListServersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.listed_servers
    import aws_sdk_transfer.types.next_token


class ListServersResponse(TypedDict):
    next_token: NotRequired["aws_sdk_transfer.types.next_token.NextToken"]
    """<p>When you can get additional results from the <code>ListServers</code> operation, a <code>NextToken</code> parameter is returned in the output. In a following command, you can pass in the <code>NextToken</code> parameter to continue listing additional servers.</p>"""
    servers: "aws_sdk_transfer.types.listed_servers.ListedServers"
    """<p>An array of servers that were listed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_transfer.types.listed_servers

    out["Servers"] = aws_sdk_transfer.types.listed_servers.serialize_aws_json_1_1(
        value["servers"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServersResponse:
    out: ListServersResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Servers" in data:
        import aws_sdk_transfer.types.listed_servers

        out["servers"] = aws_sdk_transfer.types.listed_servers.deserialize_aws_json_1_1(
            data["Servers"]
        )
    else:
        raise DeserializationError("ListServersResponse.servers required")
    return out
