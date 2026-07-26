"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#ListPackagingConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__list_of_packaging_configuration
    import capo_mediapackage_vod.types.__string


class ListPackagingConfigurationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_mediapackage_vod.types.__string.__string"]
    """A token that can be used to resume pagination from the end of the collection."""
    packaging_configurations: NotRequired[
        "capo_mediapackage_vod.types.__list_of_packaging_configuration.__listOfPackagingConfiguration"
    ]
    """A list of MediaPackage VOD PackagingConfiguration resources."""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackagingConfigurationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "packaging_configurations" in value:
        import capo_mediapackage_vod.types.__list_of_packaging_configuration

        out["packagingConfigurations"] = (
            capo_mediapackage_vod.types.__list_of_packaging_configuration.serialize_json(
                value["packaging_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListPackagingConfigurationsResponse:
    out: ListPackagingConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "packagingConfigurations" in data:
        import capo_mediapackage_vod.types.__list_of_packaging_configuration

        out["packaging_configurations"] = (
            capo_mediapackage_vod.types.__list_of_packaging_configuration.deserialize_json(
                data["packagingConfigurations"]
            )
        )
    return out
