"""Generated from Smithy shape ``com.amazonaws.ivs#ListStreamsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.pagination_token
    import aws_sdk_ivs.types.stream_list


class ListStreamsResponse(TypedDict, closed=True):
    streams: "aws_sdk_ivs.types.stream_list.StreamList"
    """<p>List of streams.</p>"""
    next_token: NotRequired["aws_sdk_ivs.types.pagination_token.PaginationToken"]
    """<p>If there are more streams than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamsResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs.types.stream_list

    out["streams"] = aws_sdk_ivs.types.stream_list.serialize_json(value["streams"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStreamsResponse:
    out: ListStreamsResponse = {}  # type: ignore[typeddict-item]
    if "streams" in data:
        import aws_sdk_ivs.types.stream_list

        out["streams"] = aws_sdk_ivs.types.stream_list.deserialize_json(data["streams"])
    else:
        raise DeserializationError("ListStreamsResponse.streams required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
