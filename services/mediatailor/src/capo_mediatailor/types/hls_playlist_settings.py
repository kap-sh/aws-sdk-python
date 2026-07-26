"""Generated from Smithy shape ``com.amazonaws.mediatailor#HlsPlaylistSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__integer
    import capo_mediatailor.types.ad_markup_types


class HlsPlaylistSettings(TypedDict, closed=True):
    manifest_window_seconds: NotRequired["capo_mediatailor.types.__integer.__integer"]
    """<p>The total duration (in seconds) of each manifest. Minimum value: <code>30</code> seconds. Maximum value: <code>3600</code> seconds.</p>"""
    ad_markup_type: NotRequired["capo_mediatailor.types.ad_markup_types.adMarkupTypes"]
    """<p>Determines the type of SCTE 35 tags to use in ad markup. Specify <code>DATERANGE</code> to use <code>DATERANGE</code> tags (for live or VOD content). Specify <code>SCTE35_ENHANCED</code> to use <code>EXT-X-CUE-OUT</code> and <code>EXT-X-CUE-IN</code> tags (for VOD content only).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HlsPlaylistSettings) -> dict:
    out: dict = {}
    if "manifest_window_seconds" in value:
        out["ManifestWindowSeconds"] = value["manifest_window_seconds"]
    if "ad_markup_type" in value:
        import capo_mediatailor.types.ad_markup_types

        out["AdMarkupType"] = capo_mediatailor.types.ad_markup_types.serialize_json(
            value["ad_markup_type"]
        )
    return out


def deserialize_json(data: dict) -> HlsPlaylistSettings:
    out: HlsPlaylistSettings = {}  # type: ignore[typeddict-item]
    if "ManifestWindowSeconds" in data:
        out["manifest_window_seconds"] = data["ManifestWindowSeconds"]
    if "AdMarkupType" in data:
        import capo_mediatailor.types.ad_markup_types

        out["ad_markup_type"] = capo_mediatailor.types.ad_markup_types.deserialize_json(
            data["AdMarkupType"]
        )
    return out
