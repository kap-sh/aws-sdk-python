"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetConnectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connection_list
    import aws_sdk_networkmanager.types.next_token


class GetConnectionsResponse(TypedDict, closed=True):
    connections: NotRequired[
        "aws_sdk_networkmanager.types.connection_list.ConnectionList"
    ]
    """<p>Information about the connections.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token to use for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectionsResponse) -> dict:
    out: dict = {}
    if "connections" in value:
        import aws_sdk_networkmanager.types.connection_list

        out["Connections"] = (
            aws_sdk_networkmanager.types.connection_list.serialize_json(
                value["connections"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetConnectionsResponse:
    out: GetConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "Connections" in data:
        import aws_sdk_networkmanager.types.connection_list

        out["connections"] = (
            aws_sdk_networkmanager.types.connection_list.deserialize_json(
                data["Connections"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
