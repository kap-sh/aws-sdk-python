"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#SuccessfulRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcampaigns.types.successful_request

SuccessfulRequestList: TypeAlias = list[
    "capo_connectcampaigns.types.successful_request.SuccessfulRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulRequestList) -> list:
    import capo_connectcampaigns.types.successful_request

    out: list = []
    for item in value:
        out.append(capo_connectcampaigns.types.successful_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> SuccessfulRequestList:
    import capo_connectcampaigns.types.successful_request

    out: SuccessfulRequestList = []
    for item in data:
        out.append(
            capo_connectcampaigns.types.successful_request.deserialize_json(item)
        )
    return out
