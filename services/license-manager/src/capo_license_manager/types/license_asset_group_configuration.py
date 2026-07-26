"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseAssetGroupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string


class LicenseAssetGroupConfiguration(TypedDict, closed=True):
    usage_dimension: NotRequired["capo_license_manager.types.string.String"]
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
