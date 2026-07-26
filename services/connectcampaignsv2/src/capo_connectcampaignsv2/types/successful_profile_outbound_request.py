"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#SuccessfulProfileOutboundRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.client_token
    import capo_connectcampaignsv2.types.profile_outbound_request_id


class SuccessfulProfileOutboundRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_connectcampaignsv2.types.client_token.ClientToken"]
    id: NotRequired[
        "capo_connectcampaignsv2.types.profile_outbound_request_id.ProfileOutboundRequestId"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulProfileOutboundRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> SuccessfulProfileOutboundRequest:
    out: SuccessfulProfileOutboundRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "id" in data:
        out["id"] = data["id"]
    return out
