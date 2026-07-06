"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    arn: "aws_sdk_connectcampaigns.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
