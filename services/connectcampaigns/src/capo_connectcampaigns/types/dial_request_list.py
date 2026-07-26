"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#DialRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcampaigns.types.dial_request

DialRequestList: TypeAlias = list[
    "capo_connectcampaigns.types.dial_request.DialRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: DialRequestList) -> list:
    import capo_connectcampaigns.types.dial_request

    out: list = []
    for item in value:
        out.append(capo_connectcampaigns.types.dial_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> DialRequestList:
    import capo_connectcampaigns.types.dial_request

    out: DialRequestList = []
    for item in data:
        out.append(capo_connectcampaigns.types.dial_request.deserialize_json(item))
    return out
