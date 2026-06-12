"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#FailedRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.failed_request

FailedRequestList: TypeAlias = list[
    "aws_sdk_connectcampaignsv2.types.failed_request.FailedRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedRequestList) -> list:
    import aws_sdk_connectcampaignsv2.types.failed_request

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcampaignsv2.types.failed_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> FailedRequestList:
    import aws_sdk_connectcampaignsv2.types.failed_request

    out: FailedRequestList = []
    for item in data:
        out.append(
            aws_sdk_connectcampaignsv2.types.failed_request.deserialize_json(item)
        )
    return out
