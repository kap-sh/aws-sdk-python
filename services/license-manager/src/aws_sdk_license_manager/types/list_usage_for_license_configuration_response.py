"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListUsageForLicenseConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.license_configuration_usage_list
    import aws_sdk_license_manager.types.string


class ListUsageForLicenseConfigurationResponse(TypedDict):
    license_configuration_usage_list: NotRequired[
        "aws_sdk_license_manager.types.license_configuration_usage_list.LicenseConfigurationUsageList"
    ]
    """<p>Information about the license configurations.</p>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsageForLicenseConfigurationResponse) -> dict:
    out: dict = {}
    if "license_configuration_usage_list" in value:
        import aws_sdk_license_manager.types.license_configuration_usage_list

        out["LicenseConfigurationUsageList"] = (
            aws_sdk_license_manager.types.license_configuration_usage_list.serialize_aws_json_1_1(
                value["license_configuration_usage_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsageForLicenseConfigurationResponse:
    out: ListUsageForLicenseConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "LicenseConfigurationUsageList" in data:
        import aws_sdk_license_manager.types.license_configuration_usage_list

        out["license_configuration_usage_list"] = (
            aws_sdk_license_manager.types.license_configuration_usage_list.deserialize_aws_json_1_1(
                data["LicenseConfigurationUsageList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
