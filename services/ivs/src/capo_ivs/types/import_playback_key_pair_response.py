"""Generated from Smithy shape ``com.amazonaws.ivs#ImportPlaybackKeyPairResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.playback_key_pair


class ImportPlaybackKeyPairResponse(TypedDict, closed=True):
    key_pair: NotRequired["capo_ivs.types.playback_key_pair.PlaybackKeyPair"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportPlaybackKeyPairResponse) -> dict:
    out: dict = {}
    if "key_pair" in value:
        import capo_ivs.types.playback_key_pair

        out["keyPair"] = capo_ivs.types.playback_key_pair.serialize_json(
            value["key_pair"]
        )
    return out


def deserialize_json(data: dict) -> ImportPlaybackKeyPairResponse:
    out: ImportPlaybackKeyPairResponse = {}  # type: ignore[typeddict-item]
    if "keyPair" in data:
        import capo_ivs.types.playback_key_pair

        out["key_pair"] = capo_ivs.types.playback_key_pair.deserialize_json(
            data["keyPair"]
        )
    return out
