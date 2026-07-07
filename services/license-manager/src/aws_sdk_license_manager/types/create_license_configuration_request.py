"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.box_boolean
    import aws_sdk_license_manager.types.box_long
    import aws_sdk_license_manager.types.license_counting_type
    import aws_sdk_license_manager.types.product_information_list
    import aws_sdk_license_manager.types.string
    import aws_sdk_license_manager.types.string_list
    import aws_sdk_license_manager.types.tag_list


class CreateLicenseConfigurationRequest(TypedDict, closed=True):
    name: "aws_sdk_license_manager.types.string.String"
    """<p>Name of the license configuration.</p>"""
    description: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Description of the license configuration.</p>"""
    license_counting_type: (
        "aws_sdk_license_manager.types.license_counting_type.LicenseCountingType"
    )
    """<p>Dimension used to track the license inventory.</p>"""
    license_count: NotRequired["aws_sdk_license_manager.types.box_long.BoxLong"]
    """<p>Number of licenses managed by the license configuration.</p>"""
    license_count_hard_limit: NotRequired[
        "aws_sdk_license_manager.types.box_boolean.BoxBoolean"
    ]
    """<p>Indicates whether hard or soft license enforcement is used. Exceeding a hard limit blocks the launch of new instances.</p>"""
    license_rules: NotRequired["aws_sdk_license_manager.types.string_list.StringList"]
    """<p>License rules. The syntax is #name=value (for example, #allowedTenancy=EC2-DedicatedHost). The available rules vary by dimension, as follows.</p> <ul> <li> <p> <code>Cores</code> dimension: <code>allowedTenancy</code> | <code>licenseAffinityToHost</code> | <code>maximumCores</code> | <code>minimumCores</code> </p> </li> <li> <p> <code>Instances</code> dimension: <code>allowedTenancy</code> | <code>maximumVcpus</code> | <code>minimumVcpus</code> </p> </li> <li> <p> <code>Sockets</code> dimension: <code>allowedTenancy</code> | <code>licenseAffinityToHost</code> | <code>maximumSockets</code> | <code>minimumSockets</code> </p> </li> <li> <p> <code>vCPUs</code> dimension: <code>allowedTenancy</code> | <code>honorVcpuOptimization</code> | <code>maximumVcpus</code> | <code>minimumVcpus</code> </p> </li> </ul> <p>The unit for <code>licenseAffinityToHost</code> is days and the range is 1 to 180. The possible values for <code>allowedTenancy</code> are <code>EC2-Default</code>, <code>EC2-DedicatedHost</code>, and <code>EC2-DedicatedInstance</code>. The possible values for <code>honorVcpuOptimization</code> are <code>True</code> and <code>False</code>.</p>"""
    tags: NotRequired["aws_sdk_license_manager.types.tag_list.TagList"]
    """<p>Tags to add to the license configuration.</p>"""
    disassociate_when_not_found: NotRequired[
        "aws_sdk_license_manager.types.box_boolean.BoxBoolean"
    ]
    """<p>When true, disassociates a resource when software is uninstalled.</p>"""
    product_information_list: NotRequired[
        "aws_sdk_license_manager.types.product_information_list.ProductInformationList"
    ]
    """<p>Product information.</p>"""
    license_expiry: NotRequired["aws_sdk_license_manager.types.box_long.BoxLong"]
    """<p>License configuration expiry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLicenseConfigurationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_license_manager.types.license_counting_type

    out["LicenseCountingType"] = (
        aws_sdk_license_manager.types.license_counting_type.serialize_aws_json_1_1(
            value["license_counting_type"]
        )
    )
    if "license_count" in value:
        out["LicenseCount"] = value["license_count"]
    if "license_count_hard_limit" in value:
        out["LicenseCountHardLimit"] = value["license_count_hard_limit"]
    if "license_rules" in value:
        import aws_sdk_license_manager.types.string_list

        out["LicenseRules"] = (
            aws_sdk_license_manager.types.string_list.serialize_aws_json_1_1(
                value["license_rules"]
            )
        )
    if "tags" in value:
        import aws_sdk_license_manager.types.tag_list

        out["Tags"] = aws_sdk_license_manager.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "disassociate_when_not_found" in value:
        out["DisassociateWhenNotFound"] = value["disassociate_when_not_found"]
    if "product_information_list" in value:
        import aws_sdk_license_manager.types.product_information_list

        out["ProductInformationList"] = (
            aws_sdk_license_manager.types.product_information_list.serialize_aws_json_1_1(
                value["product_information_list"]
            )
        )
    if "license_expiry" in value:
        out["LicenseExpiry"] = value["license_expiry"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLicenseConfigurationRequest:
    out: CreateLicenseConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateLicenseConfigurationRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "LicenseCountingType" in data:
        import aws_sdk_license_manager.types.license_counting_type

        out["license_counting_type"] = (
            aws_sdk_license_manager.types.license_counting_type.deserialize_aws_json_1_1(
                data["LicenseCountingType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLicenseConfigurationRequest.license_counting_type required"
        )
    if "LicenseCount" in data:
        out["license_count"] = data["LicenseCount"]
    if "LicenseCountHardLimit" in data:
        out["license_count_hard_limit"] = data["LicenseCountHardLimit"]
    if "LicenseRules" in data:
        import aws_sdk_license_manager.types.string_list

        out["license_rules"] = (
            aws_sdk_license_manager.types.string_list.deserialize_aws_json_1_1(
                data["LicenseRules"]
            )
        )
    if "Tags" in data:
        import aws_sdk_license_manager.types.tag_list

        out["tags"] = aws_sdk_license_manager.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "DisassociateWhenNotFound" in data:
        out["disassociate_when_not_found"] = data["DisassociateWhenNotFound"]
    if "ProductInformationList" in data:
        import aws_sdk_license_manager.types.product_information_list

        out["product_information_list"] = (
            aws_sdk_license_manager.types.product_information_list.deserialize_aws_json_1_1(
                data["ProductInformationList"]
            )
        )
    if "LicenseExpiry" in data:
        out["license_expiry"] = data["LicenseExpiry"]
    return out
