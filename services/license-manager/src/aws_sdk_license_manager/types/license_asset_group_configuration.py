"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseAssetGroupConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.string


class LicenseAssetGroupConfiguration(TypedDict):
    usage_dimension: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>License Asset Group Configuration Usage dimension.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseAssetGroupConfiguration) -> dict:
    out: dict = {}
    if "usage_dimension" in value:
        out["UsageDimension"] = value["usage_dimension"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseAssetGroupConfiguration:
    out: LicenseAssetGroupConfiguration = {}  # type: ignore[typeddict-item]
    if "UsageDimension" in data:
        out["usage_dimension"] = data["UsageDimension"]
    return out
