"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListAssetsForLicenseAssetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.asset_list
    import aws_sdk_license_manager.types.string


class ListAssetsForLicenseAssetGroupResponse(TypedDict, closed=True):
    assets: NotRequired["aws_sdk_license_manager.types.asset_list.AssetList"]
    """<p>Assets.</p>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssetsForLicenseAssetGroupResponse) -> dict:
    out: dict = {}
    if "assets" in value:
        import aws_sdk_license_manager.types.asset_list

        out["Assets"] = aws_sdk_license_manager.types.asset_list.serialize_aws_json_1_1(
            value["assets"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssetsForLicenseAssetGroupResponse:
    out: ListAssetsForLicenseAssetGroupResponse = {}  # type: ignore[typeddict-item]
    if "Assets" in data:
        import aws_sdk_license_manager.types.asset_list

        out["assets"] = (
            aws_sdk_license_manager.types.asset_list.deserialize_aws_json_1_1(
                data["Assets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
