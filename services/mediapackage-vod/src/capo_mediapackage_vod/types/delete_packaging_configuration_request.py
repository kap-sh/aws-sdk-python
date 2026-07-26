"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#DeletePackagingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__string


class DeletePackagingConfigurationRequest(TypedDict, closed=True):
    id: "capo_mediapackage_vod.types.__string.__string"
    """The ID of the MediaPackage VOD PackagingConfiguration resource to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePackagingConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePackagingConfigurationRequest:
    out: DeletePackagingConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
