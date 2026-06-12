"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListLicenseConfigurationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.box_integer
    import aws_sdk_license_manager.types.filters
    import aws_sdk_license_manager.types.string
    import aws_sdk_license_manager.types.string_list


class ListLicenseConfigurationsRequest(TypedDict):
    license_configuration_arns: NotRequired[
        "aws_sdk_license_manager.types.string_list.StringList"
    ]
    """<p>Amazon Resource Names (ARN) of the license configurations.</p>"""
    max_results: NotRequired["aws_sdk_license_manager.types.box_integer.BoxInteger"]
    """<p>Maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""
    filters: NotRequired["aws_sdk_license_manager.types.filters.Filters"]
    """<p>Filters to scope the results. The following filters and logical operators are supported:</p> <ul> <li> <p> <code>licenseCountingType</code> - The dimension for which licenses are counted. Possible values are <code>vCPU</code> | <code>Instance</code> | <code>Core</code> | <code>Socket</code>.</p> </li> <li> <p> <code>enforceLicenseCount</code> - A Boolean value that indicates whether hard license enforcement is used.</p> </li> <li> <p> <code>usagelimitExceeded</code> - A Boolean value that indicates whether the available licenses have been exceeded.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLicenseConfigurationsRequest) -> dict:
    out: dict = {}
    if "license_configuration_arns" in value:
        import aws_sdk_license_manager.types.string_list

        out["LicenseConfigurationArns"] = (
            aws_sdk_license_manager.types.string_list.serialize_aws_json_1_1(
                value["license_configuration_arns"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> ListLicenseConfigurationsRequest:
    out: ListLicenseConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "LicenseConfigurationArns" in data:
        import aws_sdk_license_manager.types.string_list

        out["license_configuration_arns"] = (
            aws_sdk_license_manager.types.string_list.deserialize_aws_json_1_1(
                data["LicenseConfigurationArns"]
            )
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
