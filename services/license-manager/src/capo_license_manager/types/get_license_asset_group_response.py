"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetLicenseAssetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.license_asset_group


class GetLicenseAssetGroupResponse(TypedDict, closed=True):
    license_asset_group: (
        "capo_license_manager.types.license_asset_group.LicenseAssetGroup"
    )
    """<p>License asset group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLicenseAssetGroupResponse) -> dict:
    out: dict = {}
    import capo_license_manager.types.license_asset_group

    out["LicenseAssetGroup"] = (
        capo_license_manager.types.license_asset_group.serialize_aws_json_1_1(
            value["license_asset_group"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLicenseAssetGroupResponse:
    out: GetLicenseAssetGroupResponse = {}  # type: ignore[typeddict-item]
    if "LicenseAssetGroup" in data:
        import capo_license_manager.types.license_asset_group

        out["license_asset_group"] = (
            capo_license_manager.types.license_asset_group.deserialize_aws_json_1_1(
                data["LicenseAssetGroup"]
            )
        )
    else:
        raise DeserializationError(
            "GetLicenseAssetGroupResponse.license_asset_group required"
        )
    return out
