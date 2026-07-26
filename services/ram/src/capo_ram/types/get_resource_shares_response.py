"""Generated from Smithy shape ``com.amazonaws.ram#GetResourceSharesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.resource_share_list
    import capo_ram.types.string


class GetResourceSharesResponse(TypedDict, closed=True):
    resource_shares: NotRequired["capo_ram.types.resource_share_list.ResourceShareList"]
    """<p>An array of objects that contain the information about the resource shares.</p>"""
    next_token: NotRequired["capo_ram.types.string.String"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceSharesResponse) -> dict:
    out: dict = {}
    if "resource_shares" in value:
        import capo_ram.types.resource_share_list

        out["resourceShares"] = capo_ram.types.resource_share_list.serialize_json(
            value["resource_shares"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetResourceSharesResponse:
    out: GetResourceSharesResponse = {}  # type: ignore[typeddict-item]
    if "resourceShares" in data:
        import capo_ram.types.resource_share_list

        out["resource_shares"] = capo_ram.types.resource_share_list.deserialize_json(
            data["resourceShares"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
