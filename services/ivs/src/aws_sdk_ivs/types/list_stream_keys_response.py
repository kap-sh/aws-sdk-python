"""Generated from Smithy shape ``com.amazonaws.ivs#ListStreamKeysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.pagination_token
    import aws_sdk_ivs.types.stream_key_list


class ListStreamKeysResponse(TypedDict, closed=True):
    stream_keys: "aws_sdk_ivs.types.stream_key_list.StreamKeyList"
    """<p>List of stream keys.</p>"""
    next_token: NotRequired["aws_sdk_ivs.types.pagination_token.PaginationToken"]
    """<p>If there are more stream keys than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamKeysResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs.types.stream_key_list

    out["streamKeys"] = aws_sdk_ivs.types.stream_key_list.serialize_json(
        value["stream_keys"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStreamKeysResponse:
    out: ListStreamKeysResponse = {}  # type: ignore[typeddict-item]
    if "streamKeys" in data:
        import aws_sdk_ivs.types.stream_key_list

        out["stream_keys"] = aws_sdk_ivs.types.stream_key_list.deserialize_json(
            data["streamKeys"]
        )
    else:
        raise DeserializationError("ListStreamKeysResponse.stream_keys required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
