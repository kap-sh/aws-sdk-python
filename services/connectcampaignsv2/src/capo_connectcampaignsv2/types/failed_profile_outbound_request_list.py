"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#FailedProfileOutboundRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.failed_profile_outbound_request

FailedProfileOutboundRequestList: TypeAlias = list[
    "capo_connectcampaignsv2.types.failed_profile_outbound_request.FailedProfileOutboundRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedProfileOutboundRequestList) -> list:
    import capo_connectcampaignsv2.types.failed_profile_outbound_request

    out: list = []
    for item in value:
        out.append(
            capo_connectcampaignsv2.types.failed_profile_outbound_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FailedProfileOutboundRequestList:
    import capo_connectcampaignsv2.types.failed_profile_outbound_request

    out: FailedProfileOutboundRequestList = []
    for item in data:
        out.append(
            capo_connectcampaignsv2.types.failed_profile_outbound_request.deserialize_json(
                item
            )
        )
    return out
