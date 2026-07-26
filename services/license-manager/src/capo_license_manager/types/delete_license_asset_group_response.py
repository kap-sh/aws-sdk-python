"""Generated from Smithy shape ``com.amazonaws.licensemanager#DeleteLicenseAssetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.license_asset_group_status


class DeleteLicenseAssetGroupResponse(TypedDict, closed=True):
    status: (
        "capo_license_manager.types.license_asset_group_status.LicenseAssetGroupStatus"
    )
    """<p>License asset group status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLicenseAssetGroupResponse) -> dict:
    out: dict = {}
    import capo_license_manager.types.license_asset_group_status

    out["Status"] = (
        capo_license_manager.types.license_asset_group_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLicenseAssetGroupResponse:
    out: DeleteLicenseAssetGroupResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_license_manager.types.license_asset_group_status

        out["status"] = (
            capo_license_manager.types.license_asset_group_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("DeleteLicenseAssetGroupResponse.status required")
    return out
