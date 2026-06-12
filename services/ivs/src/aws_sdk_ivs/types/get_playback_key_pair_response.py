"""Generated from Smithy shape ``com.amazonaws.ivs#GetPlaybackKeyPairResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs.types.playback_key_pair


class GetPlaybackKeyPairResponse(TypedDict):
    key_pair: NotRequired["aws_sdk_ivs.types.playback_key_pair.PlaybackKeyPair"]


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaybackKeyPairResponse) -> dict:
    out: dict = {}
    if "key_pair" in value:
        import aws_sdk_ivs.types.playback_key_pair

        out["keyPair"] = aws_sdk_ivs.types.playback_key_pair.serialize_json(
            value["key_pair"]
        )
    return out


def deserialize_json(data: dict) -> GetPlaybackKeyPairResponse:
    out: GetPlaybackKeyPairResponse = {}  # type: ignore[typeddict-item]
    if "keyPair" in data:
        import aws_sdk_ivs.types.playback_key_pair

        out["key_pair"] = aws_sdk_ivs.types.playback_key_pair.deserialize_json(
            data["keyPair"]
        )
    return out
