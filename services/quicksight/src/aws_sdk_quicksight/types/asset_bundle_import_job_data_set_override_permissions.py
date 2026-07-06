"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSetOverridePermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_resource_permissions
    import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list


class AssetBundleImportJobDataSetOverridePermissions(TypedDict, closed=True):
    data_set_ids: "aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of dataset IDs that you want to apply overrides to. You can use <code>*</code> to override all datasets in this asset bundle.</p>"""
    permissions: "aws_sdk_quicksight.types.asset_bundle_resource_permissions.AssetBundleResourcePermissions"
    """<p>A list of permissions for the datasets that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSetOverridePermissions) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["DataSetIds"] = (
        aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["data_set_ids"]
        )
    )
    import aws_sdk_quicksight.types.asset_bundle_resource_permissions

    out["Permissions"] = (
        aws_sdk_quicksight.types.asset_bundle_resource_permissions.serialize_json(
            value["permissions"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobDataSetOverridePermissions:
    out: AssetBundleImportJobDataSetOverridePermissions = {}  # type: ignore[typeddict-item]
    if "DataSetIds" in data:
        import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["data_set_ids"] = (
            aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["DataSetIds"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleImportJobDataSetOverridePermissions.data_set_ids required"
        )
    if "Permissions" in data:
        import aws_sdk_quicksight.types.asset_bundle_resource_permissions

        out["permissions"] = (
            aws_sdk_quicksight.types.asset_bundle_resource_permissions.deserialize_json(
                data["Permissions"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleImportJobDataSetOverridePermissions.permissions required"
        )
    return out
