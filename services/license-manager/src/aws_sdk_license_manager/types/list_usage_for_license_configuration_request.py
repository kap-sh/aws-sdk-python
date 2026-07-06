"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListUsageForLicenseConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.box_integer
    import aws_sdk_license_manager.types.filters
    import aws_sdk_license_manager.types.string


class ListUsageForLicenseConfigurationRequest(TypedDict, closed=True):
    license_configuration_arn: "aws_sdk_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the license configuration.</p>"""
    max_results: NotRequired["aws_sdk_license_manager.types.box_integer.BoxInteger"]
    """<p>Maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""
    filters: NotRequired["aws_sdk_license_manager.types.filters.Filters"]
    """<p>Filters to scope the results. The following filters and logical operators are supported:</p> <ul> <li> <p> <code>resourceArn</code> - The ARN of the license configuration resource.</p> </li> <li> <p> <code>resourceType</code> - The resource type (<code>EC2_INSTANCE</code> | <code>EC2_HOST</code> | <code>EC2_AMI</code> | <code>SYSTEMS_MANAGER_MANAGED_INSTANCE</code>).</p> </li> <li> <p> <code>resourceAccount</code> - The ID of the account that owns the resource.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsageForLicenseConfigurationRequest) -> dict:
    out: dict = {}
    out["LicenseConfigurationArn"] = value["license_configuration_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_license_manager.types.filters

        out["Filters"] = aws_sdk_license_manager.types.filters.serialize_aws_json_1_1(
            value["filters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsageForLicenseConfigurationRequest:
    out: ListUsageForLicenseConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "LicenseConfigurationArn" in data:
        out["license_configuration_arn"] = data["LicenseConfigurationArn"]
    else:
        raise DeserializationError(
            "ListUsageForLicenseConfigurationRequest.license_configuration_arn required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import aws_sdk_license_manager.types.filters

        out["filters"] = aws_sdk_license_manager.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    return out
