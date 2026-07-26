"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetLicenseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.license


class GetLicenseResponse(TypedDict, closed=True):
    license: NotRequired["capo_license_manager.types.license.License"]
    """<p>License details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLicenseResponse) -> dict:
    out: dict = {}
    if "license" in value:
        import capo_license_manager.types.license

        out["License"] = capo_license_manager.types.license.serialize_aws_json_1_1(
            value["license"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLicenseResponse:
    out: GetLicenseResponse = {}  # type: ignore[typeddict-item]
    if "License" in data:
        import capo_license_manager.types.license

        out["license"] = capo_license_manager.types.license.deserialize_aws_json_1_1(
            data["License"]
        )
    return out
