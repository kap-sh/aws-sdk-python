"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSourceOverrideTags``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list
    import aws_sdk_quicksight.types.tag_list


class AssetBundleImportJobDataSourceOverrideTags(TypedDict):
    data_source_ids: "aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of data source IDs that you want to apply overrides to. You can use <code>*</code> to override all data sources in this asset bundle.</p>"""
    tags: "aws_sdk_quicksight.types.tag_list.TagList"
    """<p>A list of tags for the data source that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSourceOverrideTags) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["DataSourceIds"] = (
        aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["data_source_ids"]
        )
    )
    import aws_sdk_quicksight.types.tag_list

    out["Tags"] = aws_sdk_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobDataSourceOverrideTags:
    out: AssetBundleImportJobDataSourceOverrideTags = {}  # type: ignore[typeddict-item]
    if "DataSourceIds" in data:
        import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["data_source_ids"] = (
            aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["DataSourceIds"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleImportJobDataSourceOverrideTags.data_source_ids required"
        )
    if "Tags" in data:
        import aws_sdk_quicksight.types.tag_list

        out["tags"] = aws_sdk_quicksight.types.tag_list.deserialize_json(data["Tags"])
    else:
        raise DeserializationError(
            "AssetBundleImportJobDataSourceOverrideTags.tags required"
        )
    return out
