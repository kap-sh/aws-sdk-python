"""Generated from Smithy shape ``com.amazonaws.ivs#ListChannelsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.channel_list
    import aws_sdk_ivs.types.pagination_token


class ListChannelsResponse(TypedDict):
    channels: "aws_sdk_ivs.types.channel_list.ChannelList"
    """<p>List of the matching channels.</p>"""
    next_token: NotRequired["aws_sdk_ivs.types.pagination_token.PaginationToken"]
    """<p>If there are more channels than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs.types.channel_list

    out["channels"] = aws_sdk_ivs.types.channel_list.serialize_json(value["channels"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelsResponse:
    out: ListChannelsResponse = {}  # type: ignore[typeddict-item]
    if "channels" in data:
        import aws_sdk_ivs.types.channel_list

        out["channels"] = aws_sdk_ivs.types.channel_list.deserialize_json(
            data["channels"]
        )
    else:
        raise DeserializationError("ListChannelsResponse.channels required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
