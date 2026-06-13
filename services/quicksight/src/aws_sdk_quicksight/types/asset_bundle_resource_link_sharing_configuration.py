"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleResourceLinkSharingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_resource_permissions


class AssetBundleResourceLinkSharingConfiguration(TypedDict):
    permissions: NotRequired[
        "aws_sdk_quicksight.types.asset_bundle_resource_permissions.AssetBundleResourcePermissions"
    ]
    """<p>A list of link sharing permissions for the dashboards that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleResourceLinkSharingConfiguration) -> dict:
    out: dict = {}
    if "permissions" in value:
        import aws_sdk_quicksight.types.asset_bundle_resource_permissions

        out["Permissions"] = (
            aws_sdk_quicksight.types.asset_bundle_resource_permissions.serialize_json(
                value["permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetBundleResourceLinkSharingConfiguration:
    out: AssetBundleResourceLinkSharingConfiguration = {}  # type: ignore[typeddict-item]
    if "Permissions" in data:
        import aws_sdk_quicksight.types.asset_bundle_resource_permissions

        out["permissions"] = (
            aws_sdk_quicksight.types.asset_bundle_resource_permissions.deserialize_json(
                data["Permissions"]
            )
        )
    return out
