"""Generated from Smithy shape ``com.amazonaws.licensemanager#UpdateLicenseConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.box_boolean
    import aws_sdk_license_manager.types.box_long
    import aws_sdk_license_manager.types.license_configuration_status
    import aws_sdk_license_manager.types.product_information_list
    import aws_sdk_license_manager.types.string
    import aws_sdk_license_manager.types.string_list


class UpdateLicenseConfigurationRequest(TypedDict, closed=True):
    license_configuration_arn: "aws_sdk_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the license configuration.</p>"""
    license_configuration_status: NotRequired[
        "aws_sdk_license_manager.types.license_configuration_status.LicenseConfigurationStatus"
    ]
    """<p>New status of the license configuration.</p>"""
    license_rules: NotRequired["aws_sdk_license_manager.types.string_list.StringList"]
    """<p>New license rule. The only rule that you can add after you create a license configuration is licenseAffinityToHost.</p>"""
    license_count: NotRequired["aws_sdk_license_manager.types.box_long.BoxLong"]
    """<p>New number of licenses managed by the license configuration.</p>"""
    license_count_hard_limit: NotRequired[
        "aws_sdk_license_manager.types.box_boolean.BoxBoolean"
    ]
    """<p>New hard limit of the number of available licenses.</p>"""
    name: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>New name of the license configuration.</p>"""
    description: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>New description of the license configuration.</p>"""
    product_information_list: NotRequired[
        "aws_sdk_license_manager.types.product_information_list.ProductInformationList"
    ]
    """<p>New product information.</p>"""
    disassociate_when_not_found: NotRequired[
        "aws_sdk_license_manager.types.box_boolean.BoxBoolean"
    ]
    """<p>When true, disassociates a resource when software is uninstalled.</p>"""
    license_expiry: NotRequired["aws_sdk_license_manager.types.box_long.BoxLong"]
    """<p>License configuration expiry time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLicenseConfigurationRequest) -> dict:
    out: dict = {}
    out["LicenseConfigurationArn"] = value["license_configuration_arn"]
    if "license_configuration_status" in value:
        import aws_sdk_license_manager.types.license_configuration_status

        out["LicenseConfigurationStatus"] = (
            aws_sdk_license_manager.types.license_configuration_status.serialize_aws_json_1_1(
                value["license_configuration_status"]
            )
        )
    if "license_rules" in value:
        import aws_sdk_license_manager.types.string_list

        out["LicenseRules"] = (
            aws_sdk_license_manager.types.string_list.serialize_aws_json_1_1(
                value["license_rules"]
            )
        )
    if "license_count" in value:
        out["LicenseCount"] = value["license_count"]
    if "license_count_hard_limit" in value:
        out["LicenseCountHardLimit"] = value["license_count_hard_limit"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "product_information_list" in value:
        import aws_sdk_license_manager.types.product_information_list

        out["ProductInformationList"] = (
            aws_sdk_license_manager.types.product_information_list.serialize_aws_json_1_1(
                value["product_information_list"]
            )
        )
    if "disassociate_when_not_found" in value:
        out["DisassociateWhenNotFound"] = value["disassociate_when_not_found"]
    if "license_expiry" in value:
        out["LicenseExpiry"] = value["license_expiry"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLicenseConfigurationRequest:
    out: UpdateLicenseConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "LicenseConfigurationArn" in data:
        out["license_configuration_arn"] = data["LicenseConfigurationArn"]
    else:
        raise DeserializationError(
            "UpdateLicenseConfigurationRequest.license_configuration_arn required"
        )
    if "LicenseConfigurationStatus" in data:
        import aws_sdk_license_manager.types.license_configuration_status

        out["license_configuration_status"] = (
            aws_sdk_license_manager.types.license_configuration_status.deserialize_aws_json_1_1(
                data["LicenseConfigurationStatus"]
            )
        )
    if "LicenseRules" in data:
        import aws_sdk_license_manager.types.string_list

        out["license_rules"] = (
            aws_sdk_license_manager.types.string_list.deserialize_aws_json_1_1(
                data["LicenseRules"]
            )
        )
    if "LicenseCount" in data:
        out["license_count"] = data["LicenseCount"]
    if "LicenseCountHardLimit" in data:
        out["license_count_hard_limit"] = data["LicenseCountHardLimit"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ProductInformationList" in data:
        import aws_sdk_license_manager.types.product_information_list

        out["product_information_list"] = (
            aws_sdk_license_manager.types.product_information_list.deserialize_aws_json_1_1(
                data["ProductInformationList"]
            )
        )
    if "DisassociateWhenNotFound" in data:
        out["disassociate_when_not_found"] = data["DisassociateWhenNotFound"]
    if "LicenseExpiry" in data:
        out["license_expiry"] = data["LicenseExpiry"]
    return out
