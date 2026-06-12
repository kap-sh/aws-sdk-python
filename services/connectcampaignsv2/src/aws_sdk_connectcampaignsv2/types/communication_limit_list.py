"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CommunicationLimitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.communication_limit

CommunicationLimitList: TypeAlias = list[
    "aws_sdk_connectcampaignsv2.types.communication_limit.CommunicationLimit"
]


# --- restJson1 ser/de ---
def serialize_json(value: CommunicationLimitList) -> list:
    import aws_sdk_connectcampaignsv2.types.communication_limit

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connectcampaignsv2.types.communication_limit.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CommunicationLimitList:
    import aws_sdk_connectcampaignsv2.types.communication_limit

    out: CommunicationLimitList = []
    for item in data:
        out.append(
            aws_sdk_connectcampaignsv2.types.communication_limit.deserialize_json(item)
        )
    return out
