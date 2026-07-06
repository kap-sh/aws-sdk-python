"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobVPCConnectionOverrideTags``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list
    import aws_sdk_quicksight.types.tag_list


class AssetBundleImportJobVPCConnectionOverrideTags(TypedDict, closed=True):
    vpc_connection_ids: "aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of VPC connection IDs that you want to apply overrides to. You can use <code>*</code> to override all VPC connections in this asset bundle.</p>"""
    tags: "aws_sdk_quicksight.types.tag_list.TagList"
    """<p>A list of tags for the VPC connections that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobVPCConnectionOverrideTags) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["VPCConnectionIds"] = (
        aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["vpc_connection_ids"]
        )
    )
    import aws_sdk_quicksight.types.tag_list

    out["Tags"] = aws_sdk_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobVPCConnectionOverrideTags:
    out: AssetBundleImportJobVPCConnectionOverrideTags = {}  # type: ignore[typeddict-item]
    if "VPCConnectionIds" in data:
        import aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["vpc_connection_ids"] = (
            aws_sdk_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["VPCConnectionIds"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleImportJobVPCConnectionOverrideTags.vpc_connection_ids required"
        )
    if "Tags" in data:
        import aws_sdk_quicksight.types.tag_list

        out["tags"] = aws_sdk_quicksight.types.tag_list.deserialize_json(data["Tags"])
    else:
        raise DeserializationError(
            "AssetBundleImportJobVPCConnectionOverrideTags.tags required"
        )
    return out
