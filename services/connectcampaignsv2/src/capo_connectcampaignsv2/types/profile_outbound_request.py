"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ProfileOutboundRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.client_token
    import capo_connectcampaignsv2.types.profile_id
    import capo_connectcampaignsv2.types.time_stamp


class ProfileOutboundRequest(TypedDict, closed=True):
    client_token: "capo_connectcampaignsv2.types.client_token.ClientToken"
    profile_id: "capo_connectcampaignsv2.types.profile_id.ProfileId"
    expiration_time: NotRequired["capo_connectcampaignsv2.types.time_stamp.TimeStamp"]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileOutboundRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["profileId"] = value["profile_id"]
    if "expiration_time" in value:
        import capo_connectcampaignsv2.types.time_stamp

        out["expirationTime"] = capo_connectcampaignsv2.types.time_stamp.serialize_json(
            value["expiration_time"]
        )
    return out


def deserialize_json(data: dict) -> ProfileOutboundRequest:
    out: ProfileOutboundRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("ProfileOutboundRequest.client_token required")
    if "profileId" in data:
        out["profile_id"] = data["profileId"]
    else:
        raise DeserializationError("ProfileOutboundRequest.profile_id required")
    if "expirationTime" in data:
        import capo_connectcampaignsv2.types.time_stamp

        out["expiration_time"] = (
            capo_connectcampaignsv2.types.time_stamp.deserialize_json(
                data["expirationTime"]
            )
        )
    return out
