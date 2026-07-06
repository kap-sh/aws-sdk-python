"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDashboardOverrideTags``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list
    import aws_sdk_quicksight.types.tag_list


class AssetBundleImportJobDashboardOverrideTags(TypedDict, closed=True):
    dashboard_ids: "aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of dashboard IDs that you want to apply overrides to. You can use <code>*</code> to override all dashboards in this asset bundle.</p>"""
    tags: "aws_sdk_quicksight.types.tag_list.TagList"
    """<p>A list of tags for the dashboards that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDashboardOverrideTags) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["DashboardIds"] = (
        aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["dashboard_ids"]
        )
    )
    import aws_sdk_quicksight.types.tag_list

    out["Tags"] = aws_sdk_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobDashboardOverrideTags:
    out: AssetBundleImportJobDashboardOverrideTags = {}  # type: ignore[typeddict-item]
    if "DashboardIds" in data:
        import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["dashboard_ids"] = (
            aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["DashboardIds"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleImportJobDashboardOverrideTags.dashboard_ids required"
        )
    if "Tags" in data:
        import aws_sdk_quicksight.types.tag_list

        out["tags"] = aws_sdk_quicksight.types.tag_list.deserialize_json(data["Tags"])
    else:
        raise DeserializationError(
            "AssetBundleImportJobDashboardOverrideTags.tags required"
        )
    return out
