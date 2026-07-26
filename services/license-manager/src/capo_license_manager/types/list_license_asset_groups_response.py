"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListLicenseAssetGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.license_asset_group_list
    import capo_license_manager.types.string


class ListLicenseAssetGroupsResponse(TypedDict, closed=True):
    license_asset_groups: NotRequired[
        "capo_license_manager.types.license_asset_group_list.LicenseAssetGroupList"
    ]
    """<p>License asset groups.</p>"""
    next_token: NotRequired["capo_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLicenseAssetGroupsResponse) -> dict:
    out: dict = {}
    if "license_asset_groups" in value:
        import capo_license_manager.types.license_asset_group_list

        out["LicenseAssetGroups"] = (
            capo_license_manager.types.license_asset_group_list.serialize_aws_json_1_1(
                value["license_asset_groups"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLicenseAssetGroupsResponse:
    out: ListLicenseAssetGroupsResponse = {}  # type: ignore[typeddict-item]
    if "LicenseAssetGroups" in data:
        import capo_license_manager.types.license_asset_group_list

        out["license_asset_groups"] = (
            capo_license_manager.types.license_asset_group_list.deserialize_aws_json_1_1(
                data["LicenseAssetGroups"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
