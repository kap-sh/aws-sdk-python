"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#SuccessfulProfileOutboundRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.successful_profile_outbound_request

SuccessfulProfileOutboundRequestList: TypeAlias = list[
    "aws_sdk_connectcampaignsv2.types.successful_profile_outbound_request.SuccessfulProfileOutboundRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulProfileOutboundRequestList) -> list:
    import aws_sdk_connectcampaignsv2.types.successful_profile_outbound_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connectcampaignsv2.types.successful_profile_outbound_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SuccessfulProfileOutboundRequestList:
    import aws_sdk_connectcampaignsv2.types.successful_profile_outbound_request

    out: SuccessfulProfileOutboundRequestList = []
    for item in data:
        out.append(
            aws_sdk_connectcampaignsv2.types.successful_profile_outbound_request.deserialize_json(
                item
            )
        )
    return out
