"""Generated from Smithy shape ``com.amazonaws.mediatailor#RequestOutputItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.dash_playlist_settings
    import aws_sdk_mediatailor.types.hls_playlist_settings


class RequestOutputItem(TypedDict):
    dash_playlist_settings: NotRequired[
        "aws_sdk_mediatailor.types.dash_playlist_settings.DashPlaylistSettings"
    ]
    """<p>DASH manifest configuration parameters.</p>"""
    hls_playlist_settings: NotRequired[
        "aws_sdk_mediatailor.types.hls_playlist_settings.HlsPlaylistSettings"
    ]
    """<p>HLS playlist configuration parameters.</p>"""
    manifest_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the manifest for the channel. The name appears in the <code>PlaybackUrl</code>.</p>"""
    source_group: "aws_sdk_mediatailor.types.__string.__string"
    """<p>A string used to match which <code>HttpPackageConfiguration</code> is used for each <code>VodSource</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequestOutputItem) -> dict:
    out: dict = {}
    if "dash_playlist_settings" in value:
        import aws_sdk_mediatailor.types.dash_playlist_settings

        out["DashPlaylistSettings"] = (
            aws_sdk_mediatailor.types.dash_playlist_settings.serialize_json(
                value["dash_playlist_settings"]
            )
        )
    if "hls_playlist_settings" in value:
        import aws_sdk_mediatailor.types.hls_playlist_settings

        out["HlsPlaylistSettings"] = (
            aws_sdk_mediatailor.types.hls_playlist_settings.serialize_json(
                value["hls_playlist_settings"]
            )
        )
    out["ManifestName"] = value["manifest_name"]
    out["SourceGroup"] = value["source_group"]
    return out


def deserialize_json(data: dict) -> RequestOutputItem:
    out: RequestOutputItem = {}  # type: ignore[typeddict-item]
    if "DashPlaylistSettings" in data:
        import aws_sdk_mediatailor.types.dash_playlist_settings

        out["dash_playlist_settings"] = (
            aws_sdk_mediatailor.types.dash_playlist_settings.deserialize_json(
                data["DashPlaylistSettings"]
            )
        )
    if "HlsPlaylistSettings" in data:
        import aws_sdk_mediatailor.types.hls_playlist_settings

        out["hls_playlist_settings"] = (
            aws_sdk_mediatailor.types.hls_playlist_settings.deserialize_json(
                data["HlsPlaylistSettings"]
            )
        )
    if "ManifestName" in data:
        out["manifest_name"] = data["ManifestName"]
    else:
        raise DeserializationError("RequestOutputItem.manifest_name required")
    if "SourceGroup" in data:
        out["source_group"] = data["SourceGroup"]
    else:
        raise DeserializationError("RequestOutputItem.source_group required")
    return out
