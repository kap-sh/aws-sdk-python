"""Generated from Smithy shape ``com.amazonaws.medialive#MediaPackageV2DestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.hls_auto_select
    import aws_sdk_medialive.types.hls_default


class MediaPackageV2DestinationSettings(TypedDict, closed=True):
    audio_group_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Applies only to an output that contains audio. If you want to put several audio encodes into one audio rendition group, decide on a name (ID) for the group. Then in every audio output that you want to belong to that group, enter that ID in this field. Note that this information is part of the HLS specification (not the CMAF specification), but if you include it then MediaPackage will include it in the manifest it creates for the video player."""
    audio_rendition_sets: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Applies only to an output that contains video, and only if you want to associate one or more audio groups to this video. In this field you assign the groups that you create (in the Group ID fields in the various audio outputs). Enter one group ID, or enter a comma-separated list of group IDs. Note that this information is part of the HLS specification (not the CMAF specification), but if you include it then MediaPackage will include it in the manifest it creates for the video player."""
    hls_auto_select: NotRequired[
        "aws_sdk_medialive.types.hls_auto_select.HlsAutoSelect"
    ]
    """Specifies whether MediaPackage should set this output as the auto-select rendition in the HLS manifest. YES means this must be the auto-select. NO means this should never be the auto-select. OMIT means MediaPackage decides what to set on this rendition. When you consider all the renditions, follow these guidelines. You can set zero or one renditions to YES. You can set zero or more renditions to NO, but you can't set all renditions to NO. You can set zero, some, or all to OMIT."""
    hls_default: NotRequired["aws_sdk_medialive.types.hls_default.HlsDefault"]
    """Specifies whether MediaPackage should set this output as the default rendition in the HLS manifest. YES means this must be the default. NO means this should never be the default. OMIT means MediaPackage decides what to set on this rendition. When you consider all the renditions, follow these guidelines. You can set zero or one renditions to YES. You can set zero or more renditions to NO, but you can't set all renditions to NO. You can set zero, some, or all to OMIT."""


# --- restJson1 ser/de ---
def serialize_json(value: MediaPackageV2DestinationSettings) -> dict:
    out: dict = {}
    if "audio_group_id" in value:
        out["audioGroupId"] = value["audio_group_id"]
    if "audio_rendition_sets" in value:
        out["audioRenditionSets"] = value["audio_rendition_sets"]
    if "hls_auto_select" in value:
        import aws_sdk_medialive.types.hls_auto_select

        out["hlsAutoSelect"] = aws_sdk_medialive.types.hls_auto_select.serialize_json(
            value["hls_auto_select"]
        )
    if "hls_default" in value:
        import aws_sdk_medialive.types.hls_default

        out["hlsDefault"] = aws_sdk_medialive.types.hls_default.serialize_json(
            value["hls_default"]
        )
    return out


def deserialize_json(data: dict) -> MediaPackageV2DestinationSettings:
    out: MediaPackageV2DestinationSettings = {}  # type: ignore[typeddict-item]
    if "audioGroupId" in data:
        out["audio_group_id"] = data["audioGroupId"]
    if "audioRenditionSets" in data:
        out["audio_rendition_sets"] = data["audioRenditionSets"]
    if "hlsAutoSelect" in data:
        import aws_sdk_medialive.types.hls_auto_select

        out["hls_auto_select"] = (
            aws_sdk_medialive.types.hls_auto_select.deserialize_json(
                data["hlsAutoSelect"]
            )
        )
    if "hlsDefault" in data:
        import aws_sdk_medialive.types.hls_default

        out["hls_default"] = aws_sdk_medialive.types.hls_default.deserialize_json(
            data["hlsDefault"]
        )
    return out
