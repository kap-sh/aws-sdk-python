"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeSourceServersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.pagination_token
    import aws_sdk_mgn.types.source_servers_list


class DescribeSourceServersResponse(TypedDict):
    items: NotRequired["aws_sdk_mgn.types.source_servers_list.SourceServersList"]
    """<p>Request to filter Source Servers list by item.</p>"""
    next_token: NotRequired["aws_sdk_mgn.types.pagination_token.PaginationToken"]
    """<p>Request to filter Source Servers next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSourceServersResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_mgn.types.source_servers_list

        out["items"] = aws_sdk_mgn.types.source_servers_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeSourceServersResponse:
    out: DescribeSourceServersResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_mgn.types.source_servers_list

        out["items"] = aws_sdk_mgn.types.source_servers_list.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
