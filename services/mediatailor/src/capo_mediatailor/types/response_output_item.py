"""Generated from Smithy shape ``com.amazonaws.mediatailor#ResponseOutputItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.dash_playlist_settings
    import capo_mediatailor.types.hls_playlist_settings


class ResponseOutputItem(TypedDict, closed=True):
    dash_playlist_settings: NotRequired[
        "capo_mediatailor.types.dash_playlist_settings.DashPlaylistSettings"
    ]
    """<p>DASH manifest configuration settings.</p>"""
    hls_playlist_settings: NotRequired[
        "capo_mediatailor.types.hls_playlist_settings.HlsPlaylistSettings"
    ]
    """<p>HLS manifest configuration settings.</p>"""
    manifest_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the manifest for the channel that will appear in the channel output's playback URL.</p>"""
    playback_url: "capo_mediatailor.types.__string.__string"
    """<p>The URL used for playback by content players.</p>"""
    source_group: "capo_mediatailor.types.__string.__string"
    """<p>A string used to associate a package configuration source group with a channel output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseOutputItem) -> dict:
    out: dict = {}
    if "dash_playlist_settings" in value:
        import capo_mediatailor.types.dash_playlist_settings

        out["DashPlaylistSettings"] = (
            capo_mediatailor.types.dash_playlist_settings.serialize_json(
                value["dash_playlist_settings"]
            )
        )
    if "hls_playlist_settings" in value:
        import capo_mediatailor.types.hls_playlist_settings

        out["HlsPlaylistSettings"] = (
            capo_mediatailor.types.hls_playlist_settings.serialize_json(
                value["hls_playlist_settings"]
            )
        )
    out["ManifestName"] = value["manifest_name"]
    out["PlaybackUrl"] = value["playback_url"]
    out["SourceGroup"] = value["source_group"]
    return out


def deserialize_json(data: dict) -> ResponseOutputItem:
    out: ResponseOutputItem = {}  # type: ignore[typeddict-item]
    if "DashPlaylistSettings" in data:
        import capo_mediatailor.types.dash_playlist_settings

        out["dash_playlist_settings"] = (
            capo_mediatailor.types.dash_playlist_settings.deserialize_json(
                data["DashPlaylistSettings"]
            )
        )
    if "HlsPlaylistSettings" in data:
        import capo_mediatailor.types.hls_playlist_settings

        out["hls_playlist_settings"] = (
            capo_mediatailor.types.hls_playlist_settings.deserialize_json(
                data["HlsPlaylistSettings"]
            )
        )
    if "ManifestName" in data:
        out["manifest_name"] = data["ManifestName"]
    else:
        raise DeserializationError("ResponseOutputItem.manifest_name required")
    if "PlaybackUrl" in data:
        out["playback_url"] = data["PlaybackUrl"]
    else:
        raise DeserializationError("ResponseOutputItem.playback_url required")
    if "SourceGroup" in data:
        out["source_group"] = data["SourceGroup"]
    else:
        raise DeserializationError("ResponseOutputItem.source_group required")
    return out
