"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn
    import aws_sdk_license_manager.types.client_token
    import aws_sdk_license_manager.types.consumption_configuration
    import aws_sdk_license_manager.types.datetime_range
    import aws_sdk_license_manager.types.entitlement_list
    import aws_sdk_license_manager.types.issuer
    import aws_sdk_license_manager.types.license_status
    import aws_sdk_license_manager.types.metadata_list
    import aws_sdk_license_manager.types.string


class CreateLicenseVersionRequest(TypedDict):
    license_arn: "aws_sdk_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license.</p>"""
    license_name: "aws_sdk_license_manager.types.string.String"
    """<p>License name.</p>"""
    product_name: "aws_sdk_license_manager.types.string.String"
    """<p>Product name.</p>"""
    issuer: "aws_sdk_license_manager.types.issuer.Issuer"
    """<p>License issuer.</p>"""
    home_region: "aws_sdk_license_manager.types.string.String"
    """<p>Home Region of the license.</p>"""
    validity: "aws_sdk_license_manager.types.datetime_range.DatetimeRange"
    """<p>Date and time range during which the license is valid, in ISO8601-UTC format.</p>"""
    license_metadata: NotRequired[
        "aws_sdk_license_manager.types.metadata_list.MetadataList"
    ]
    """<p>Information about the license.</p>"""
    entitlements: "aws_sdk_license_manager.types.entitlement_list.EntitlementList"
    """<p>License entitlements.</p>"""
    consumption_configuration: "aws_sdk_license_manager.types.consumption_configuration.ConsumptionConfiguration"
    """<p>Configuration for consumption of the license. Choose a provisional configuration for workloads running with continuous connectivity. Choose a borrow configuration for workloads with offline usage.</p>"""
    status: "aws_sdk_license_manager.types.license_status.LicenseStatus"
    """<p>License status.</p>"""
    client_token: "aws_sdk_license_manager.types.client_token.ClientToken"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    source_version: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Current version of the license.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLicenseVersionRequest) -> dict:
    out: dict = {}
    out["LicenseArn"] = value["license_arn"]
    out["LicenseName"] = value["license_name"]
    out["ProductName"] = value["product_name"]
    import aws_sdk_license_manager.types.issuer

    out["Issuer"] = aws_sdk_license_manager.types.issuer.serialize_aws_json_1_1(
        value["issuer"]
    )
    out["HomeRegion"] = value["home_region"]
    import aws_sdk_license_manager.types.datetime_range

    out["Validity"] = (
        aws_sdk_license_manager.types.datetime_range.serialize_aws_json_1_1(
            value["validity"]
        )
    )
    if "license_metadata" in value:
        import aws_sdk_license_manager.types.metadata_list

        out["LicenseMetadata"] = (
            aws_sdk_license_manager.types.metadata_list.serialize_aws_json_1_1(
                value["license_metadata"]
            )
        )
    import aws_sdk_license_manager.types.entitlement_list

    out["Entitlements"] = (
        aws_sdk_license_manager.types.entitlement_list.serialize_aws_json_1_1(
            value["entitlements"]
        )
    )
    import aws_sdk_license_manager.types.consumption_configuration

    out["ConsumptionConfiguration"] = (
        aws_sdk_license_manager.types.consumption_configuration.serialize_aws_json_1_1(
            value["consumption_configuration"]
        )
    )
    import aws_sdk_license_manager.types.license_status

    out["Status"] = aws_sdk_license_manager.types.license_status.serialize_aws_json_1_1(
        value["status"]
    )
    out["ClientToken"] = value["client_token"]
    if "source_version" in value:
        out["SourceVersion"] = value["source_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLicenseVersionRequest:
    out: CreateLicenseVersionRequest = {}  # type: ignore[typeddict-item]
    if "LicenseArn" in data:
        out["license_arn"] = data["LicenseArn"]
    else:
        raise DeserializationError("CreateLicenseVersionRequest.license_arn required")
    if "LicenseName" in data:
        out["license_name"] = data["LicenseName"]
    else:
        raise DeserializationError("CreateLicenseVersionRequest.license_name required")
    if "ProductName" in data:
        out["product_name"] = data["ProductName"]
    else:
        raise DeserializationError("CreateLicenseVersionRequest.product_name required")
    if "Issuer" in data:
        import aws_sdk_license_manager.types.issuer

        out["issuer"] = aws_sdk_license_manager.types.issuer.deserialize_aws_json_1_1(
            data["Issuer"]
        )
    else:
        raise DeserializationError("CreateLicenseVersionRequest.issuer required")
    if "HomeRegion" in data:
        out["home_region"] = data["HomeRegion"]
    else:
        raise DeserializationError("CreateLicenseVersionRequest.home_region required")
    if "Validity" in data:
        import aws_sdk_license_manager.types.datetime_range

        out["validity"] = (
            aws_sdk_license_manager.types.datetime_range.deserialize_aws_json_1_1(
                data["Validity"]
            )
        )
    else:
        raise DeserializationError("CreateLicenseVersionRequest.validity required")
    if "LicenseMetadata" in data:
        import aws_sdk_license_manager.types.metadata_list

        out["license_metadata"] = (
            aws_sdk_license_manager.types.metadata_list.deserialize_aws_json_1_1(
                data["LicenseMetadata"]
            )
        )
    if "Entitlements" in data:
        import aws_sdk_license_manager.types.entitlement_list

        out["entitlements"] = (
            aws_sdk_license_manager.types.entitlement_list.deserialize_aws_json_1_1(
                data["Entitlements"]
            )
        )
    else:
        raise DeserializationError("CreateLicenseVersionRequest.entitlements required")
    if "ConsumptionConfiguration" in data:
        import aws_sdk_license_manager.types.consumption_configuration

        out["consumption_configuration"] = (
            aws_sdk_license_manager.types.consumption_configuration.deserialize_aws_json_1_1(
                data["ConsumptionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLicenseVersionRequest.consumption_configuration required"
        )
    if "Status" in data:
        import aws_sdk_license_manager.types.license_status

        out["status"] = (
            aws_sdk_license_manager.types.license_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("CreateLicenseVersionRequest.status required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("CreateLicenseVersionRequest.client_token required")
    if "SourceVersion" in data:
        out["source_version"] = data["SourceVersion"]
    return out
