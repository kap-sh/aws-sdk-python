"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetLicenseConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.automated_discovery_information
    import capo_license_manager.types.box_boolean
    import capo_license_manager.types.box_long
    import capo_license_manager.types.consumed_license_summary_list
    import capo_license_manager.types.license_counting_type
    import capo_license_manager.types.managed_resource_summary_list
    import capo_license_manager.types.product_information_list
    import capo_license_manager.types.string
    import capo_license_manager.types.string_list
    import capo_license_manager.types.tag_list


class GetLicenseConfigurationResponse(TypedDict, closed=True):
    license_configuration_id: NotRequired["capo_license_manager.types.string.String"]
    """<p>Unique ID for the license configuration.</p>"""
    license_configuration_arn: NotRequired["capo_license_manager.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the license configuration.</p>"""
    name: NotRequired["capo_license_manager.types.string.String"]
    """<p>Name of the license configuration.</p>"""
    description: NotRequired["capo_license_manager.types.string.String"]
    """<p>Description of the license configuration.</p>"""
    license_counting_type: NotRequired[
        "capo_license_manager.types.license_counting_type.LicenseCountingType"
    ]
    """<p>Dimension for which the licenses are counted.</p>"""
    license_rules: NotRequired["capo_license_manager.types.string_list.StringList"]
    """<p>License rules.</p>"""
    license_count: NotRequired["capo_license_manager.types.box_long.BoxLong"]
    """<p>Number of available licenses.</p>"""
    license_count_hard_limit: NotRequired[
        "capo_license_manager.types.box_boolean.BoxBoolean"
    ]
    """<p>Sets the number of available licenses as a hard limit.</p>"""
    consumed_licenses: NotRequired["capo_license_manager.types.box_long.BoxLong"]
    """<p>Number of licenses assigned to resources.</p>"""
    status: NotRequired["capo_license_manager.types.string.String"]
    """<p>License configuration status.</p>"""
    owner_account_id: NotRequired["capo_license_manager.types.string.String"]
    """<p>Account ID of the owner of the license configuration.</p>"""
    consumed_license_summary_list: NotRequired[
        "capo_license_manager.types.consumed_license_summary_list.ConsumedLicenseSummaryList"
    ]
    """<p>Summaries of the licenses consumed by resources.</p>"""
    managed_resource_summary_list: NotRequired[
        "capo_license_manager.types.managed_resource_summary_list.ManagedResourceSummaryList"
    ]
    """<p>Summaries of the managed resources.</p>"""
    tags: NotRequired["capo_license_manager.types.tag_list.TagList"]
    """<p>Tags for the license configuration.</p>"""
    product_information_list: NotRequired[
        "capo_license_manager.types.product_information_list.ProductInformationList"
    ]
    """<p>Product information.</p>"""
    automated_discovery_information: NotRequired[
        "capo_license_manager.types.automated_discovery_information.AutomatedDiscoveryInformation"
    ]
    """<p>Automated discovery information.</p>"""
    disassociate_when_not_found: NotRequired[
        "capo_license_manager.types.box_boolean.BoxBoolean"
    ]
    """<p>When true, disassociates a resource when software is uninstalled.</p>"""
    license_expiry: NotRequired["capo_license_manager.types.box_long.BoxLong"]
    """<p>License Expiry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLicenseConfigurationResponse) -> dict:
    out: dict = {}
    if "license_configuration_id" in value:
        out["LicenseConfigurationId"] = value["license_configuration_id"]
    if "license_configuration_arn" in value:
        out["LicenseConfigurationArn"] = value["license_configuration_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "license_counting_type" in value:
        import capo_license_manager.types.license_counting_type

        out["LicenseCountingType"] = (
            capo_license_manager.types.license_counting_type.serialize_aws_json_1_1(
                value["license_counting_type"]
            )
        )
    if "license_rules" in value:
        import capo_license_manager.types.string_list

        out["LicenseRules"] = (
            capo_license_manager.types.string_list.serialize_aws_json_1_1(
                value["license_rules"]
            )
        )
    if "license_count" in value:
        out["LicenseCount"] = value["license_count"]
    if "license_count_hard_limit" in value:
        out["LicenseCountHardLimit"] = value["license_count_hard_limit"]
    if "consumed_licenses" in value:
        out["ConsumedLicenses"] = value["consumed_licenses"]
    if "status" in value:
        out["Status"] = value["status"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "consumed_license_summary_list" in value:
        import capo_license_manager.types.consumed_license_summary_list

        out["ConsumedLicenseSummaryList"] = (
            capo_license_manager.types.consumed_license_summary_list.serialize_aws_json_1_1(
                value["consumed_license_summary_list"]
            )
        )
    if "managed_resource_summary_list" in value:
        import capo_license_manager.types.managed_resource_summary_list

        out["ManagedResourceSummaryList"] = (
            capo_license_manager.types.managed_resource_summary_list.serialize_aws_json_1_1(
                value["managed_resource_summary_list"]
            )
        )
    if "tags" in value:
        import capo_license_manager.types.tag_list

        out["Tags"] = capo_license_manager.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "product_information_list" in value:
        import capo_license_manager.types.product_information_list

        out["ProductInformationList"] = (
            capo_license_manager.types.product_information_list.serialize_aws_json_1_1(
                value["product_information_list"]
            )
        )
    if "automated_discovery_information" in value:
        import capo_license_manager.types.automated_discovery_information

        out["AutomatedDiscoveryInformation"] = (
            capo_license_manager.types.automated_discovery_information.serialize_aws_json_1_1(
                value["automated_discovery_information"]
            )
        )
    if "disassociate_when_not_found" in value:
        out["DisassociateWhenNotFound"] = value["disassociate_when_not_found"]
    if "license_expiry" in value:
        out["LicenseExpiry"] = value["license_expiry"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLicenseConfigurationResponse:
    out: GetLicenseConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "LicenseConfigurationId" in data:
        out["license_configuration_id"] = data["LicenseConfigurationId"]
    if "LicenseConfigurationArn" in data:
        out["license_configuration_arn"] = data["LicenseConfigurationArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LicenseCountingType" in data:
        import capo_license_manager.types.license_counting_type

        out["license_counting_type"] = (
            capo_license_manager.types.license_counting_type.deserialize_aws_json_1_1(
                data["LicenseCountingType"]
            )
        )
    if "LicenseRules" in data:
        import capo_license_manager.types.string_list

        out["license_rules"] = (
            capo_license_manager.types.string_list.deserialize_aws_json_1_1(
                data["LicenseRules"]
            )
        )
    if "LicenseCount" in data:
        out["license_count"] = data["LicenseCount"]
    if "LicenseCountHardLimit" in data:
        out["license_count_hard_limit"] = data["LicenseCountHardLimit"]
    if "ConsumedLicenses" in data:
        out["consumed_licenses"] = data["ConsumedLicenses"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "OwnerAccountId" in data:
        out["owner_account_id"] = data["OwnerAccountId"]
    if "ConsumedLicenseSummaryList" in data:
        import capo_license_manager.types.consumed_license_summary_list

        out["consumed_license_summary_list"] = (
            capo_license_manager.types.consumed_license_summary_list.deserialize_aws_json_1_1(
                data["ConsumedLicenseSummaryList"]
            )
        )
    if "ManagedResourceSummaryList" in data:
        import capo_license_manager.types.managed_resource_summary_list

        out["managed_resource_summary_list"] = (
            capo_license_manager.types.managed_resource_summary_list.deserialize_aws_json_1_1(
                data["ManagedResourceSummaryList"]
            )
        )
    if "Tags" in data:
        import capo_license_manager.types.tag_list

        out["tags"] = capo_license_manager.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "ProductInformationList" in data:
        import capo_license_manager.types.product_information_list

        out["product_information_list"] = (
            capo_license_manager.types.product_information_list.deserialize_aws_json_1_1(
                data["ProductInformationList"]
            )
        )
    if "AutomatedDiscoveryInformation" in data:
        import capo_license_manager.types.automated_discovery_information

        out["automated_discovery_information"] = (
            capo_license_manager.types.automated_discovery_information.deserialize_aws_json_1_1(
                data["AutomatedDiscoveryInformation"]
            )
        )
    if "DisassociateWhenNotFound" in data:
        out["disassociate_when_not_found"] = data["DisassociateWhenNotFound"]
    if "LicenseExpiry" in data:
        out["license_expiry"] = data["LicenseExpiry"]
    return out
