"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#OutboundRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.outbound_request

OutboundRequestList: TypeAlias = list[
    "aws_sdk_connectcampaignsv2.types.outbound_request.OutboundRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutboundRequestList) -> list:
    import aws_sdk_connectcampaignsv2.types.outbound_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connectcampaignsv2.types.outbound_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OutboundRequestList:
    import aws_sdk_connectcampaignsv2.types.outbound_request

    out: OutboundRequestList = []
    for item in data:
        out.append(
            aws_sdk_connectcampaignsv2.types.outbound_request.deserialize_json(item)
        )
    return out
