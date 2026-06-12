"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#DialRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.dial_request

DialRequestList: TypeAlias = list[
    "aws_sdk_connectcampaigns.types.dial_request.DialRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: DialRequestList) -> list:
    import aws_sdk_connectcampaigns.types.dial_request

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcampaigns.types.dial_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> DialRequestList:
    import aws_sdk_connectcampaigns.types.dial_request

    out: DialRequestList = []
    for item in data:
        out.append(aws_sdk_connectcampaigns.types.dial_request.deserialize_json(item))
    return out
