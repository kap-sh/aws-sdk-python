"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#MssPackage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__integer
    import capo_mediapackage_vod.types.__list_of_mss_manifest
    import capo_mediapackage_vod.types.mss_encryption


class MssPackage(TypedDict, closed=True):
    encryption: NotRequired["capo_mediapackage_vod.types.mss_encryption.MssEncryption"]
    mss_manifests: NotRequired[
        "capo_mediapackage_vod.types.__list_of_mss_manifest.__listOfMssManifest"
    ]
    """A list of MSS manifest configurations."""
    segment_duration_seconds: NotRequired[
        "capo_mediapackage_vod.types.__integer.__integer"
    ]
    """The duration (in seconds) of each segment."""


# --- restJson1 ser/de ---
def serialize_json(value: MssPackage) -> dict:
    out: dict = {}
    if "encryption" in value:
        import capo_mediapackage_vod.types.mss_encryption

        out["encryption"] = capo_mediapackage_vod.types.mss_encryption.serialize_json(
            value["encryption"]
        )
    if "mss_manifests" in value:
        import capo_mediapackage_vod.types.__list_of_mss_manifest

        out["mssManifests"] = (
            capo_mediapackage_vod.types.__list_of_mss_manifest.serialize_json(
                value["mss_manifests"]
            )
        )
    if "segment_duration_seconds" in value:
        out["segmentDurationSeconds"] = value["segment_duration_seconds"]
    return out


def deserialize_json(data: dict) -> MssPackage:
    out: MssPackage = {}  # type: ignore[typeddict-item]
    if "encryption" in data:
        import capo_mediapackage_vod.types.mss_encryption

        out["encryption"] = capo_mediapackage_vod.types.mss_encryption.deserialize_json(
            data["encryption"]
        )
    if "mssManifests" in data:
        import capo_mediapackage_vod.types.__list_of_mss_manifest

        out["mss_manifests"] = (
            capo_mediapackage_vod.types.__list_of_mss_manifest.deserialize_json(
                data["mssManifests"]
            )
        )
    if "segmentDurationSeconds" in data:
        out["segment_duration_seconds"] = data["segmentDurationSeconds"]
    return out
