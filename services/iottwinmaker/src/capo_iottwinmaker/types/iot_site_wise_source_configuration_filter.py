"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#IotSiteWiseSourceConfigurationFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iottwinmaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.filter_by_asset
    import capo_iottwinmaker.types.filter_by_asset_model


class _IotSiteWiseSourceConfigurationFilter_filterByAssetModel(TypedDict, closed=True):
    filterByAssetModel: (
        "capo_iottwinmaker.types.filter_by_asset_model.FilterByAssetModel"
    )


class _IotSiteWiseSourceConfigurationFilter_filterByAsset(TypedDict, closed=True):
    filterByAsset: "capo_iottwinmaker.types.filter_by_asset.FilterByAsset"


IotSiteWiseSourceConfigurationFilter: TypeAlias = (
    _IotSiteWiseSourceConfigurationFilter_filterByAssetModel
    | _IotSiteWiseSourceConfigurationFilter_filterByAsset
)


# --- restJson1 ser/de ---
def serialize_json(value: IotSiteWiseSourceConfigurationFilter) -> dict:
    if "filterByAssetModel" in value:
        import capo_iottwinmaker.types.filter_by_asset_model

        return {
            "filterByAssetModel": capo_iottwinmaker.types.filter_by_asset_model.serialize_json(
                value["filterByAssetModel"]
            )
        }
    elif "filterByAsset" in value:
        import capo_iottwinmaker.types.filter_by_asset

        return {
            "filterByAsset": capo_iottwinmaker.types.filter_by_asset.serialize_json(
                value["filterByAsset"]
            )
        }
    else:
        raise SerializationError(
            "IotSiteWiseSourceConfigurationFilter: no variant present"
        )


def deserialize_json(data: dict) -> IotSiteWiseSourceConfigurationFilter:
    if "filterByAssetModel" in data:
        import capo_iottwinmaker.types.filter_by_asset_model

        return {
            "filterByAssetModel": capo_iottwinmaker.types.filter_by_asset_model.deserialize_json(
                data["filterByAssetModel"]
            )
        }
    elif "filterByAsset" in data:
        import capo_iottwinmaker.types.filter_by_asset

        return {
            "filterByAsset": capo_iottwinmaker.types.filter_by_asset.deserialize_json(
                data["filterByAsset"]
            )
        }
    else:
        raise DeserializationError(
            "IotSiteWiseSourceConfigurationFilter: no recognized variant key"
        )
