"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcampaigns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.arn
    import aws_sdk_connectcampaigns.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    arn: "aws_sdk_connectcampaigns.types.arn.Arn"
    tags: "aws_sdk_connectcampaigns.types.tag_map.TagMap"


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaigns.types.tag_map

    out["tags"] = aws_sdk_connectcampaigns.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_connectcampaigns.types.tag_map

        out["tags"] = aws_sdk_connectcampaigns.types.tag_map.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
