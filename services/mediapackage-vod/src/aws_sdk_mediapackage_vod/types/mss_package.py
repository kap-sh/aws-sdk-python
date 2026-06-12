"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#MssPackage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__integer
    import aws_sdk_mediapackage_vod.types.__list_of_mss_manifest
    import aws_sdk_mediapackage_vod.types.mss_encryption


class MssPackage(TypedDict):
    encryption: NotRequired[
        "aws_sdk_mediapackage_vod.types.mss_encryption.MssEncryption"
    ]
    mss_manifests: NotRequired[
        "aws_sdk_mediapackage_vod.types.__list_of_mss_manifest.__listOfMssManifest"
    ]
    """A list of MSS manifest configurations."""
    segment_duration_seconds: NotRequired[
        "aws_sdk_mediapackage_vod.types.__integer.__integer"
    ]
    """The duration (in seconds) of each segment."""


# --- restJson1 ser/de ---
def serialize_json(value: MssPackage) -> dict:
    out: dict = {}
    if "encryption" in value:
        import aws_sdk_mediapackage_vod.types.mss_encryption

        out["encryption"] = (
            aws_sdk_mediapackage_vod.types.mss_encryption.serialize_json(
                value["encryption"]
            )
        )
    if "mss_manifests" in value:
        import aws_sdk_mediapackage_vod.types.__list_of_mss_manifest

        out["mssManifests"] = (
            aws_sdk_mediapackage_vod.types.__list_of_mss_manifest.serialize_json(
                value["mss_manifests"]
            )
        )
    if "segment_duration_seconds" in value:
        out["segmentDurationSeconds"] = value["segment_duration_seconds"]
    return out


def deserialize_json(data: dict) -> MssPackage:
    out: MssPackage = {}  # type: ignore[typeddict-item]
    if "encryption" in data:
        import aws_sdk_mediapackage_vod.types.mss_encryption

        out["encryption"] = (
            aws_sdk_mediapackage_vod.types.mss_encryption.deserialize_json(
                data["encryption"]
            )
        )
    if "mssManifests" in data:
        import aws_sdk_mediapackage_vod.types.__list_of_mss_manifest

        out["mss_manifests"] = (
            aws_sdk_mediapackage_vod.types.__list_of_mss_manifest.deserialize_json(
                data["mssManifests"]
            )
        )
    if "segmentDurationSeconds" in data:
        out["segment_duration_seconds"] = data["segmentDurationSeconds"]
    return out
