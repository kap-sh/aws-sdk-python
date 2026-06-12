"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeVcenterClientsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mgn.types.pagination_token
    import aws_sdk_mgn.types.vcenter_client_list

class DescribeVcenterClientsResponse(TypedDict):
    items: NotRequired["aws_sdk_mgn.types.vcenter_client_list.VcenterClientList"]
    """<p>List of items returned by DescribeVcenterClients.</p>"""
    next_token: NotRequired["aws_sdk_mgn.types.pagination_token.PaginationToken"]
    """<p>Next pagination token returned from DescribeVcenterClients.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DescribeVcenterClientsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_mgn.types.vcenter_client_list
        out["items"] = aws_sdk_mgn.types.vcenter_client_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeVcenterClientsResponse:
    out: DescribeVcenterClientsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_mgn.types.vcenter_client_list
        out["items"] = aws_sdk_mgn.types.vcenter_client_list.deserialize_json(data["items"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out