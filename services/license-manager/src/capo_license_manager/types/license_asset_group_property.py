"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseAssetGroupProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.string


class LicenseAssetGroupProperty(TypedDict, closed=True):
    key: "capo_license_manager.types.string.String"
    """<p>Property key.</p>"""
    value: "capo_license_manager.types.string.String"
    """<p>Property value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseAssetGroupProperty) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseAssetGroupProperty:
    out: LicenseAssetGroupProperty = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("LicenseAssetGroupProperty.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("LicenseAssetGroupProperty.value required")
    return out
