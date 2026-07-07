"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListPeeringsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.next_token
    import aws_sdk_networkmanager.types.peering_list


class ListPeeringsResponse(TypedDict, closed=True):
    peerings: NotRequired["aws_sdk_networkmanager.types.peering_list.PeeringList"]
    """<p>Lists the transit gateway peerings for the <code>ListPeerings</code> request.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPeeringsResponse) -> dict:
    out: dict = {}
    if "peerings" in value:
        import aws_sdk_networkmanager.types.peering_list

        out["Peerings"] = aws_sdk_networkmanager.types.peering_list.serialize_json(
            value["peerings"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPeeringsResponse:
    out: ListPeeringsResponse = {}  # type: ignore[typeddict-item]
    if "Peerings" in data:
        import aws_sdk_networkmanager.types.peering_list

        out["peerings"] = aws_sdk_networkmanager.types.peering_list.deserialize_json(
            data["Peerings"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
