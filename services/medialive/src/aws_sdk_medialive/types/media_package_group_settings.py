"""Generated from Smithy shape ``com.amazonaws.medialive#MediaPackageGroupSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.media_package_v2_group_settings
    import aws_sdk_medialive.types.output_location_ref


class MediaPackageGroupSettings(TypedDict):
    destination: NotRequired[
        "aws_sdk_medialive.types.output_location_ref.OutputLocationRef"
    ]
    """MediaPackage channel destination."""
    mediapackage_v2_group_settings: NotRequired[
        "aws_sdk_medialive.types.media_package_v2_group_settings.MediaPackageV2GroupSettings"
    ]
    """Parameters that apply only if the destination parameter (for the output group) specifies a channelGroup and channelName. Use of these two paramters indicates that the output group is for MediaPackage V2 (CMAF Ingest)."""


# --- restJson1 ser/de ---
def serialize_json(value: MediaPackageGroupSettings) -> dict:
    out: dict = {}
    if "destination" in value:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = aws_sdk_medialive.types.output_location_ref.serialize_json(
            value["destination"]
        )
    if "mediapackage_v2_group_settings" in value:
        import aws_sdk_medialive.types.media_package_v2_group_settings

        out["mediapackageV2GroupSettings"] = (
            aws_sdk_medialive.types.media_package_v2_group_settings.serialize_json(
                value["mediapackage_v2_group_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaPackageGroupSettings:
    out: MediaPackageGroupSettings = {}  # type: ignore[typeddict-item]
    if "destination" in data:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = (
            aws_sdk_medialive.types.output_location_ref.deserialize_json(
                data["destination"]
            )
        )
    if "mediapackageV2GroupSettings" in data:
        import aws_sdk_medialive.types.media_package_v2_group_settings

        out["mediapackage_v2_group_settings"] = (
            aws_sdk_medialive.types.media_package_v2_group_settings.deserialize_json(
                data["mediapackageV2GroupSettings"]
            )
        )
    return out
