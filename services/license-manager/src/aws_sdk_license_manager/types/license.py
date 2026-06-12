"""Generated from Smithy shape ``com.amazonaws.licensemanager#License``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn
    import aws_sdk_license_manager.types.consumption_configuration
    import aws_sdk_license_manager.types.datetime_range
    import aws_sdk_license_manager.types.entitlement_list
    import aws_sdk_license_manager.types.iso8601_date_time
    import aws_sdk_license_manager.types.issuer_details
    import aws_sdk_license_manager.types.license_status
    import aws_sdk_license_manager.types.metadata_list
    import aws_sdk_license_manager.types.string


class License(TypedDict):
    license_arn: NotRequired["aws_sdk_license_manager.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the license.</p>"""
    license_name: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>License name.</p>"""
    product_name: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Product name.</p>"""
    product_sku: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Product SKU.</p>"""
    issuer: NotRequired["aws_sdk_license_manager.types.issuer_details.IssuerDetails"]
    """<p>License issuer.</p>"""
    home_region: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Home Region of the license.</p>"""
    status: NotRequired["aws_sdk_license_manager.types.license_status.LicenseStatus"]
    """<p>License status.</p>"""
    validity: NotRequired["aws_sdk_license_manager.types.datetime_range.DatetimeRange"]
    """<p>Date and time range during which the license is valid, in ISO8601-UTC format.</p>"""
    beneficiary: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>License beneficiary.</p>"""
    entitlements: NotRequired[
        "aws_sdk_license_manager.types.entitlement_list.EntitlementList"
    ]
    """<p>License entitlements.</p>"""
    consumption_configuration: NotRequired[
        "aws_sdk_license_manager.types.consumption_configuration.ConsumptionConfiguration"
    ]
    """<p>Configuration for consumption of the license.</p>"""
    license_metadata: NotRequired[
        "aws_sdk_license_manager.types.metadata_list.MetadataList"
    ]
    """<p>License metadata.</p>"""
    create_time: NotRequired[
        "aws_sdk_license_manager.types.iso8601_date_time.ISO8601DateTime"
    ]
    """<p>License creation time.</p>"""
    version: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>License version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: License) -> dict:
    out: dict = {}
    if "license_arn" in value:
        out["LicenseArn"] = value["license_arn"]
    if "license_name" in value:
        out["LicenseName"] = value["license_name"]
    if "product_name" in value:
        out["ProductName"] = value["product_name"]
    if "product_sku" in value:
        out["ProductSKU"] = value["product_sku"]
    if "issuer" in value:
        import aws_sdk_license_manager.types.issuer_details

        out["Issuer"] = (
            aws_sdk_license_manager.types.issuer_details.serialize_aws_json_1_1(
                value["issuer"]
            )
        )
    if "home_region" in value:
        out["HomeRegion"] = value["home_region"]
    if "status" in value:
        import aws_sdk_license_manager.types.license_status

        out["Status"] = (
            aws_sdk_license_manager.types.license_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "validity" in value:
        import aws_sdk_license_manager.types.datetime_range

        out["Validity"] = (
            aws_sdk_license_manager.types.datetime_range.serialize_aws_json_1_1(
                value["validity"]
            )
        )
    if "beneficiary" in value:
        out["Beneficiary"] = value["beneficiary"]
    if "entitlements" in value:
        import aws_sdk_license_manager.types.entitlement_list

        out["Entitlements"] = (
            aws_sdk_license_manager.types.entitlement_list.serialize_aws_json_1_1(
                value["entitlements"]
            )
        )
    if "consumption_configuration" in value:
        import aws_sdk_license_manager.types.consumption_configuration

        out["ConsumptionConfiguration"] = (
            aws_sdk_license_manager.types.consumption_configuration.serialize_aws_json_1_1(
                value["consumption_configuration"]
            )
        )
    if "license_metadata" in value:
        import aws_sdk_license_manager.types.metadata_list

        out["LicenseMetadata"] = (
            aws_sdk_license_manager.types.metadata_list.serialize_aws_json_1_1(
                value["license_metadata"]
            )
        )
    if "create_time" in value:
        out["CreateTime"] = value["create_time"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> License:
    out: License = {}  # type: ignore[typeddict-item]
    if "LicenseArn" in data:
        out["license_arn"] = data["LicenseArn"]
    if "LicenseName" in data:
        out["license_name"] = data["LicenseName"]
    if "ProductName" in data:
        out["product_name"] = data["ProductName"]
    if "ProductSKU" in data:
        out["product_sku"] = data["ProductSKU"]
    if "Issuer" in data:
        import aws_sdk_license_manager.types.issuer_details

        out["issuer"] = (
            aws_sdk_license_manager.types.issuer_details.deserialize_aws_json_1_1(
                data["Issuer"]
            )
        )
    if "HomeRegion" in data:
        out["home_region"] = data["HomeRegion"]
    if "Status" in data:
        import aws_sdk_license_manager.types.license_status

        out["status"] = (
            aws_sdk_license_manager.types.license_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Validity" in data:
        import aws_sdk_license_manager.types.datetime_range

        out["validity"] = (
            aws_sdk_license_manager.types.datetime_range.deserialize_aws_json_1_1(
                data["Validity"]
            )
        )
    if "Beneficiary" in data:
        out["beneficiary"] = data["Beneficiary"]
    if "Entitlements" in data:
        import aws_sdk_license_manager.types.entitlement_list

        out["entitlements"] = (
            aws_sdk_license_manager.types.entitlement_list.deserialize_aws_json_1_1(
                data["Entitlements"]
            )
        )
    if "ConsumptionConfiguration" in data:
        import aws_sdk_license_manager.types.consumption_configuration

        out["consumption_configuration"] = (
            aws_sdk_license_manager.types.consumption_configuration.deserialize_aws_json_1_1(
                data["ConsumptionConfiguration"]
            )
        )
    if "LicenseMetadata" in data:
        import aws_sdk_license_manager.types.metadata_list

        out["license_metadata"] = (
            aws_sdk_license_manager.types.metadata_list.deserialize_aws_json_1_1(
                data["LicenseMetadata"]
            )
        )
    if "CreateTime" in data:
        out["create_time"] = data["CreateTime"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
