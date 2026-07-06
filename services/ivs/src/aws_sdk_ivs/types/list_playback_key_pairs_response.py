"""Generated from Smithy shape ``com.amazonaws.ivs#ListPlaybackKeyPairsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.pagination_token
    import aws_sdk_ivs.types.playback_key_pair_list


class ListPlaybackKeyPairsResponse(TypedDict, closed=True):
    key_pairs: "aws_sdk_ivs.types.playback_key_pair_list.PlaybackKeyPairList"
    """<p>List of key pairs.</p>"""
    next_token: NotRequired["aws_sdk_ivs.types.pagination_token.PaginationToken"]
    """<p>If there are more key pairs than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPlaybackKeyPairsResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs.types.playback_key_pair_list

    out["keyPairs"] = aws_sdk_ivs.types.playback_key_pair_list.serialize_json(
        value["key_pairs"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPlaybackKeyPairsResponse:
    out: ListPlaybackKeyPairsResponse = {}  # type: ignore[typeddict-item]
    if "keyPairs" in data:
        import aws_sdk_ivs.types.playback_key_pair_list

        out["key_pairs"] = aws_sdk_ivs.types.playback_key_pair_list.deserialize_json(
            data["keyPairs"]
        )
    else:
        raise DeserializationError("ListPlaybackKeyPairsResponse.key_pairs required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
