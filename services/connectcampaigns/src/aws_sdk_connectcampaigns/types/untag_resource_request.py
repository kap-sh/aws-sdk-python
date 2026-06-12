"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.arn
    import aws_sdk_connectcampaigns.types.tag_key_list


class UntagResourceRequest(TypedDict):
    arn: "aws_sdk_connectcampaigns.types.arn.Arn"
    tag_keys: "aws_sdk_connectcampaigns.types.tag_key_list.TagKeyList"


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
