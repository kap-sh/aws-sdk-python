"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDashboardOverridePermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_resource_link_sharing_configuration
    import capo_quicksight.types.asset_bundle_resource_permissions
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list


class AssetBundleImportJobDashboardOverridePermissions(TypedDict, closed=True):
    dashboard_ids: "capo_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of dashboard IDs that you want to apply overrides to. You can use <code>*</code> to override all dashboards in this asset bundle.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.asset_bundle_resource_permissions.AssetBundleResourcePermissions"
    ]
    """<p>A list of permissions for the dashboards that you want to apply overrides to.</p>"""
    link_sharing_configuration: NotRequired[
        "capo_quicksight.types.asset_bundle_resource_link_sharing_configuration.AssetBundleResourceLinkSharingConfiguration"
    ]
    """<p>A structure that contains the link sharing configurations that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDashboardOverridePermissions) -> dict:
    out: dict = {}
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["DashboardIds"] = (
        capo_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["dashboard_ids"]
        )
    )
    if "permissions" in value:
        import capo_quicksight.types.asset_bundle_resource_permissions

        out["Permissions"] = (
            capo_quicksight.types.asset_bundle_resource_permissions.serialize_json(
                value["permissions"]
            )
        )
    if "link_sharing_configuration" in value:
        import capo_quicksight.types.asset_bundle_resource_link_sharing_configuration

        out["LinkSharingConfiguration"] = (
            capo_quicksight.types.asset_bundle_resource_link_sharing_configuration.serialize_json(
                value["link_sharing_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobDashboardOverridePermissions:
    out: AssetBundleImportJobDashboardOverridePermissions = {}  # type: ignore[typeddict-item]
    if "DashboardIds" in data:
        import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["dashboard_ids"] = (
            capo_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["DashboardIds"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleImportJobDashboardOverridePermissions.dashboard_ids required"
        )
    if "Permissions" in data:
        import capo_quicksight.types.asset_bundle_resource_permissions

        out["permissions"] = (
            capo_quicksight.types.asset_bundle_resource_permissions.deserialize_json(
                data["Permissions"]
            )
        )
    if "LinkSharingConfiguration" in data:
        import capo_quicksight.types.asset_bundle_resource_link_sharing_configuration

        out["link_sharing_configuration"] = (
            capo_quicksight.types.asset_bundle_resource_link_sharing_configuration.deserialize_json(
                data["LinkSharingConfiguration"]
            )
        )
    return out
