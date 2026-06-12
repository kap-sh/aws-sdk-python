"""Generated from Smithy shape ``com.amazonaws.mediapackage#CmafPackageCreateOrUpdateParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__integer
    import aws_sdk_mediapackage.types.__list_of_hls_manifest_create_or_update_parameters
    import aws_sdk_mediapackage.types.__string
    import aws_sdk_mediapackage.types.cmaf_encryption
    import aws_sdk_mediapackage.types.stream_selection


class CmafPackageCreateOrUpdateParameters(TypedDict):
    encryption: NotRequired["aws_sdk_mediapackage.types.cmaf_encryption.CmafEncryption"]
    hls_manifests: NotRequired[
        "aws_sdk_mediapackage.types.__list_of_hls_manifest_create_or_update_parameters.__listOfHlsManifestCreateOrUpdateParameters"
    ]
    """A list of HLS manifest configurations"""
    segment_duration_seconds: NotRequired[
        "aws_sdk_mediapackage.types.__integer.__integer"
    ]
    """Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration."""
    segment_prefix: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """An optional custom string that is prepended to the name of each segment. If not specified, it defaults to the ChannelId."""
    stream_selection: NotRequired[
        "aws_sdk_mediapackage.types.stream_selection.StreamSelection"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CmafPackageCreateOrUpdateParameters) -> dict:
    out: dict = {}
    if "encryption" in value:
        import aws_sdk_mediapackage.types.cmaf_encryption

        out["encryption"] = aws_sdk_mediapackage.types.cmaf_encryption.serialize_json(
            value["encryption"]
        )
    if "hls_manifests" in value:
        import aws_sdk_mediapackage.types.__list_of_hls_manifest_create_or_update_parameters

        out["hlsManifests"] = (
            aws_sdk_mediapackage.types.__list_of_hls_manifest_create_or_update_parameters.serialize_json(
                value["hls_manifests"]
            )
        )
    if "segment_duration_seconds" in value:
        out["segmentDurationSeconds"] = value["segment_duration_seconds"]
    if "segment_prefix" in value:
        out["segmentPrefix"] = value["segment_prefix"]
    if "stream_selection" in value:
        import aws_sdk_mediapackage.types.stream_selection

        out["streamSelection"] = (
            aws_sdk_mediapackage.types.stream_selection.serialize_json(
                value["stream_selection"]
            )
        )
    return out


def deserialize_json(data: dict) -> CmafPackageCreateOrUpdateParameters:
    out: CmafPackageCreateOrUpdateParameters = {}  # type: ignore[typeddict-item]
    if "encryption" in data:
        import aws_sdk_mediapackage.types.cmaf_encryption

        out["encryption"] = aws_sdk_mediapackage.types.cmaf_encryption.deserialize_json(
            data["encryption"]
        )
    if "hlsManifests" in data:
        import aws_sdk_mediapackage.types.__list_of_hls_manifest_create_or_update_parameters

        out["hls_manifests"] = (
            aws_sdk_mediapackage.types.__list_of_hls_manifest_create_or_update_parameters.deserialize_json(
                data["hlsManifests"]
            )
        )
    if "segmentDurationSeconds" in data:
        out["segment_duration_seconds"] = data["segmentDurationSeconds"]
    if "segmentPrefix" in data:
        out["segment_prefix"] = data["segmentPrefix"]
    if "streamSelection" in data:
        import aws_sdk_mediapackage.types.stream_selection

        out["stream_selection"] = (
            aws_sdk_mediapackage.types.stream_selection.deserialize_json(
                data["streamSelection"]
            )
        )
    return out
