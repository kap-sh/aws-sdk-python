"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ProfileOutboundRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.profile_outbound_request

ProfileOutboundRequestList: TypeAlias = list[
    "aws_sdk_connectcampaignsv2.types.profile_outbound_request.ProfileOutboundRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileOutboundRequestList) -> list:
    import aws_sdk_connectcampaignsv2.types.profile_outbound_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connectcampaignsv2.types.profile_outbound_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProfileOutboundRequestList:
    import aws_sdk_connectcampaignsv2.types.profile_outbound_request

    out: ProfileOutboundRequestList = []
    for item in data:
        out.append(
            aws_sdk_connectcampaignsv2.types.profile_outbound_request.deserialize_json(
                item
            )
        )
    return out
