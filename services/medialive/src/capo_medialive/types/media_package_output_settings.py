"""Generated from Smithy shape ``com.amazonaws.medialive#MediaPackageOutputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.media_package_v2_destination_settings


class MediaPackageOutputSettings(TypedDict, closed=True):
    media_package_v2_destination_settings: NotRequired[
        "capo_medialive.types.media_package_v2_destination_settings.MediaPackageV2DestinationSettings"
    ]
    """Optional settings for MediaPackage V2 destinations"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaPackageOutputSettings) -> dict:
    out: dict = {}
    if "media_package_v2_destination_settings" in value:
        import capo_medialive.types.media_package_v2_destination_settings

        out["mediaPackageV2DestinationSettings"] = (
            capo_medialive.types.media_package_v2_destination_settings.serialize_json(
                value["media_package_v2_destination_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaPackageOutputSettings:
    out: MediaPackageOutputSettings = {}  # type: ignore[typeddict-item]
    if "mediaPackageV2DestinationSettings" in data:
        import capo_medialive.types.media_package_v2_destination_settings

        out["media_package_v2_destination_settings"] = (
            capo_medialive.types.media_package_v2_destination_settings.deserialize_json(
                data["mediaPackageV2DestinationSettings"]
            )
        )
    return out
