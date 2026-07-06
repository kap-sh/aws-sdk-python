"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListLicenseSpecificationsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.license_specifications
    import aws_sdk_license_manager.types.string


class ListLicenseSpecificationsForResourceResponse(TypedDict, closed=True):
    license_specifications: NotRequired[
        "aws_sdk_license_manager.types.license_specifications.LicenseSpecifications"
    ]
    """<p>License configurations associated with a resource.</p>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLicenseSpecificationsForResourceResponse) -> dict:
    out: dict = {}
    if "license_specifications" in value:
        import aws_sdk_license_manager.types.license_specifications

        out["LicenseSpecifications"] = (
            aws_sdk_license_manager.types.license_specifications.serialize_aws_json_1_1(
                value["license_specifications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListLicenseSpecificationsForResourceResponse:
    out: ListLicenseSpecificationsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "LicenseSpecifications" in data:
        import aws_sdk_license_manager.types.license_specifications

        out["license_specifications"] = (
            aws_sdk_license_manager.types.license_specifications.deserialize_aws_json_1_1(
                data["LicenseSpecifications"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
