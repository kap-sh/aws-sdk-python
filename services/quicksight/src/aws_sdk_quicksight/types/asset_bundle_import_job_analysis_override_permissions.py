"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobAnalysisOverridePermissions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_resource_permissions
    import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list


class AssetBundleImportJobAnalysisOverridePermissions(TypedDict):
    analysis_ids: "aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of analysis IDs that you want to apply overrides to. You can use <code>*</code> to override all analyses in this asset bundle.</p>"""
    permissions: "aws_sdk_quicksight.types.asset_bundle_resource_permissions.AssetBundleResourcePermissions"
    """<p>A list of permissions for the analyses that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobAnalysisOverridePermissions) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["AnalysisIds"] = (
        aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["analysis_ids"]
        )
    )
    import aws_sdk_quicksight.types.asset_bundle_resource_permissions

    out["Permissions"] = (
        aws_sdk_quicksight.types.asset_bundle_resource_permissions.serialize_json(
            value["permissions"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobAnalysisOverridePermissions:
    out: AssetBundleImportJobAnalysisOverridePermissions = {}  # type: ignore[typeddict-item]
    if "AnalysisIds" in data:
        import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["analysis_ids"] = (
            aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["AnalysisIds"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleImportJobAnalysisOverridePermissions.analysis_ids required"
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
            "AssetBundleImportJobAnalysisOverridePermissions.permissions required"
        )
    return out
