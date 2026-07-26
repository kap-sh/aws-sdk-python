"""Generated from Smithy shape ``com.amazonaws.mediapackage#MssPackage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__integer
    import capo_mediapackage.types.mss_encryption
    import capo_mediapackage.types.stream_selection


class MssPackage(TypedDict, closed=True):
    encryption: NotRequired["capo_mediapackage.types.mss_encryption.MssEncryption"]
    manifest_window_seconds: NotRequired["capo_mediapackage.types.__integer.__integer"]
    """The time window (in seconds) contained in each manifest."""
    segment_duration_seconds: NotRequired["capo_mediapackage.types.__integer.__integer"]
    """The duration (in seconds) of each segment."""
    stream_selection: NotRequired[
        "capo_mediapackage.types.stream_selection.StreamSelection"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MssPackage) -> dict:
    out: dict = {}
    if "encryption" in value:
        import capo_mediapackage.types.mss_encryption

        out["encryption"] = capo_mediapackage.types.mss_encryption.serialize_json(
            value["encryption"]
        )
    if "manifest_window_seconds" in value:
        out["manifestWindowSeconds"] = value["manifest_window_seconds"]
    if "segment_duration_seconds" in value:
        out["segmentDurationSeconds"] = value["segment_duration_seconds"]
    if "stream_selection" in value:
        import capo_mediapackage.types.stream_selection

        out["streamSelection"] = (
            capo_mediapackage.types.stream_selection.serialize_json(
                value["stream_selection"]
            )
        )
    return out


def deserialize_json(data: dict) -> MssPackage:
    out: MssPackage = {}  # type: ignore[typeddict-item]
    if "encryption" in data:
        import capo_mediapackage.types.mss_encryption

        out["encryption"] = capo_mediapackage.types.mss_encryption.deserialize_json(
            data["encryption"]
        )
    if "manifestWindowSeconds" in data:
        out["manifest_window_seconds"] = data["manifestWindowSeconds"]
    if "segmentDurationSeconds" in data:
        out["segment_duration_seconds"] = data["segmentDurationSeconds"]
    if "streamSelection" in data:
        import capo_mediapackage.types.stream_selection

        out["stream_selection"] = (
            capo_mediapackage.types.stream_selection.deserialize_json(
                data["streamSelection"]
            )
        )
    return out
