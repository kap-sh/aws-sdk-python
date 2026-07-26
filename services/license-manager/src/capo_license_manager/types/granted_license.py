"""Generated from Smithy shape ``com.amazonaws.licensemanager#GrantedLicense``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.arn
    import capo_license_manager.types.consumption_configuration
    import capo_license_manager.types.datetime_range
    import capo_license_manager.types.entitlement_list
    import capo_license_manager.types.iso8601_date_time
    import capo_license_manager.types.issuer_details
    import capo_license_manager.types.license_status
    import capo_license_manager.types.metadata_list
    import capo_license_manager.types.received_metadata
    import capo_license_manager.types.string


class GrantedLicense(TypedDict, closed=True):
    license_arn: NotRequired["capo_license_manager.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the license.</p>"""
    license_name: NotRequired["capo_license_manager.types.string.String"]
    """<p>License name.</p>"""
    product_name: NotRequired["capo_license_manager.types.string.String"]
    """<p>Product name.</p>"""
    product_sku: NotRequired["capo_license_manager.types.string.String"]
    """<p>Product SKU.</p>"""
    issuer: NotRequired["capo_license_manager.types.issuer_details.IssuerDetails"]
    """<p>Granted license issuer.</p>"""
    home_region: NotRequired["capo_license_manager.types.string.String"]
    """<p>Home Region of the granted license.</p>"""
    status: NotRequired["capo_license_manager.types.license_status.LicenseStatus"]
    """<p>Granted license status.</p>"""
    validity: NotRequired["capo_license_manager.types.datetime_range.DatetimeRange"]
    """<p>Date and time range during which the granted license is valid, in ISO8601-UTC format.</p>"""
    beneficiary: NotRequired["capo_license_manager.types.string.String"]
    """<p>Granted license beneficiary.</p>"""
    entitlements: NotRequired[
        "capo_license_manager.types.entitlement_list.EntitlementList"
    ]
    """<p>License entitlements.</p>"""
    consumption_configuration: NotRequired[
        "capo_license_manager.types.consumption_configuration.ConsumptionConfiguration"
    ]
    """<p>Configuration for consumption of the license.</p>"""
    license_metadata: NotRequired[
        "capo_license_manager.types.metadata_list.MetadataList"
    ]
    """<p>Granted license metadata.</p>"""
    create_time: NotRequired[
        "capo_license_manager.types.iso8601_date_time.ISO8601DateTime"
    ]
    """<p>Creation time of the granted license.</p>"""
    version: NotRequired["capo_license_manager.types.string.String"]
    """<p>Version of the granted license.</p>"""
    received_metadata: NotRequired[
        "capo_license_manager.types.received_metadata.ReceivedMetadata"
    ]
    """<p>Granted license received metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrantedLicense) -> dict:
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
        import capo_license_manager.types.issuer_details

        out["Issuer"] = (
            capo_license_manager.types.issuer_details.serialize_aws_json_1_1(
                value["issuer"]
            )
        )
    if "home_region" in value:
        out["HomeRegion"] = value["home_region"]
    if "status" in value:
        import capo_license_manager.types.license_status

        out["Status"] = (
            capo_license_manager.types.license_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "validity" in value:
        import capo_license_manager.types.datetime_range

        out["Validity"] = (
            capo_license_manager.types.datetime_range.serialize_aws_json_1_1(
                value["validity"]
            )
        )
    if "beneficiary" in value:
        out["Beneficiary"] = value["beneficiary"]
    if "entitlements" in value:
        import capo_license_manager.types.entitlement_list

        out["Entitlements"] = (
            capo_license_manager.types.entitlement_list.serialize_aws_json_1_1(
                value["entitlements"]
            )
        )
    if "consumption_configuration" in value:
        import capo_license_manager.types.consumption_configuration

        out["ConsumptionConfiguration"] = (
            capo_license_manager.types.consumption_configuration.serialize_aws_json_1_1(
                value["consumption_configuration"]
            )
        )
    if "license_metadata" in value:
        import capo_license_manager.types.metadata_list

        out["LicenseMetadata"] = (
            capo_license_manager.types.metadata_list.serialize_aws_json_1_1(
                value["license_metadata"]
            )
        )
    if "create_time" in value:
        out["CreateTime"] = value["create_time"]
    if "version" in value:
        out["Version"] = value["version"]
    if "received_metadata" in value:
        import capo_license_manager.types.received_metadata

        out["ReceivedMetadata"] = (
            capo_license_manager.types.received_metadata.serialize_aws_json_1_1(
                value["received_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GrantedLicense:
    out: GrantedLicense = {}  # type: ignore[typeddict-item]
    if "LicenseArn" in data:
        out["license_arn"] = data["LicenseArn"]
    if "LicenseName" in data:
        out["license_name"] = data["LicenseName"]
    if "ProductName" in data:
        out["product_name"] = data["ProductName"]
    if "ProductSKU" in data:
        out["product_sku"] = data["ProductSKU"]
    if "Issuer" in data:
        import capo_license_manager.types.issuer_details

        out["issuer"] = (
            capo_license_manager.types.issuer_details.deserialize_aws_json_1_1(
                data["Issuer"]
            )
        )
    if "HomeRegion" in data:
        out["home_region"] = data["HomeRegion"]
    if "Status" in data:
        import capo_license_manager.types.license_status

        out["status"] = (
            capo_license_manager.types.license_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Validity" in data:
        import capo_license_manager.types.datetime_range

        out["validity"] = (
            capo_license_manager.types.datetime_range.deserialize_aws_json_1_1(
                data["Validity"]
            )
        )
    if "Beneficiary" in data:
        out["beneficiary"] = data["Beneficiary"]
    if "Entitlements" in data:
        import capo_license_manager.types.entitlement_list

        out["entitlements"] = (
            capo_license_manager.types.entitlement_list.deserialize_aws_json_1_1(
                data["Entitlements"]
            )
        )
    if "ConsumptionConfiguration" in data:
        import capo_license_manager.types.consumption_configuration

        out["consumption_configuration"] = (
            capo_license_manager.types.consumption_configuration.deserialize_aws_json_1_1(
                data["ConsumptionConfiguration"]
            )
        )
    if "LicenseMetadata" in data:
        import capo_license_manager.types.metadata_list

        out["license_metadata"] = (
            capo_license_manager.types.metadata_list.deserialize_aws_json_1_1(
                data["LicenseMetadata"]
            )
        )
    if "CreateTime" in data:
        out["create_time"] = data["CreateTime"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "ReceivedMetadata" in data:
        import capo_license_manager.types.received_metadata

        out["received_metadata"] = (
            capo_license_manager.types.received_metadata.deserialize_aws_json_1_1(
                data["ReceivedMetadata"]
            )
        )
    return out
