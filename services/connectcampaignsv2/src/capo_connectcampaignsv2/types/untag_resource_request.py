"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn
    import capo_connectcampaignsv2.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    arn: "capo_connectcampaignsv2.types.arn.Arn"
    tag_keys: "capo_connectcampaignsv2.types.tag_key_list.TagKeyList"


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
