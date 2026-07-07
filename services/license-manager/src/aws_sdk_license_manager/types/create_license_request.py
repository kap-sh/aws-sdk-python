"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.client_token
    import aws_sdk_license_manager.types.consumption_configuration
    import aws_sdk_license_manager.types.datetime_range
    import aws_sdk_license_manager.types.entitlement_list
    import aws_sdk_license_manager.types.issuer
    import aws_sdk_license_manager.types.metadata_list
    import aws_sdk_license_manager.types.string
    import aws_sdk_license_manager.types.tag_list


class CreateLicenseRequest(TypedDict, closed=True):
    license_name: "aws_sdk_license_manager.types.string.String"
    """<p>License name.</p>"""
    product_name: "aws_sdk_license_manager.types.string.String"
    """<p>Product name.</p>"""
    product_sku: "aws_sdk_license_manager.types.string.String"
    """<p>Product SKU.</p>"""
    issuer: "aws_sdk_license_manager.types.issuer.Issuer"
    """<p>License issuer.</p>"""
    home_region: "aws_sdk_license_manager.types.string.String"
    """<p>Home Region for the license.</p>"""
    validity: "aws_sdk_license_manager.types.datetime_range.DatetimeRange"
    """<p>Date and time range during which the license is valid, in ISO8601-UTC format.</p>"""
    entitlements: "aws_sdk_license_manager.types.entitlement_list.EntitlementList"
    """<p>License entitlements.</p>"""
    beneficiary: "aws_sdk_license_manager.types.string.String"
    """<p>License beneficiary.</p>"""
    consumption_configuration: "aws_sdk_license_manager.types.consumption_configuration.ConsumptionConfiguration"
    """<p>Configuration for consumption of the license. Choose a provisional configuration for workloads running with continuous connectivity. Choose a borrow configuration for workloads with offline usage.</p>"""
    license_metadata: NotRequired[
        "aws_sdk_license_manager.types.metadata_list.MetadataList"
    ]
    """<p>Information about the license.</p>"""
    client_token: "aws_sdk_license_manager.types.client_token.ClientToken"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tags: NotRequired["aws_sdk_license_manager.types.tag_list.TagList"]
    r"""<p>Tags to add to the license. For more information about tagging support in License Manager, see the <a href=\"https://docs.aws.amazon.com/license-manager/latest/APIReference/API_TagResource.html\">TagResource</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLicenseRequest) -> dict:
    out: dict = {}
    out["LicenseName"] = value["license_name"]
    out["ProductName"] = value["product_name"]
    out["ProductSKU"] = value["product_sku"]
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
    import aws_sdk_license_manager.types.entitlement_list

    out["Entitlements"] = (
        aws_sdk_license_manager.types.entitlement_list.serialize_aws_json_1_1(
            value["entitlements"]
        )
    )
    out["Beneficiary"] = value["beneficiary"]
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
    out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_license_manager.types.tag_list

        out["Tags"] = aws_sdk_license_manager.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLicenseRequest:
    out: CreateLicenseRequest = {}  # type: ignore[typeddict-item]
    if "LicenseName" in data:
        out["license_name"] = data["LicenseName"]
    else:
        raise DeserializationError("CreateLicenseRequest.license_name required")
    if "ProductName" in data:
        out["product_name"] = data["ProductName"]
    else:
        raise DeserializationError("CreateLicenseRequest.product_name required")
    if "ProductSKU" in data:
        out["product_sku"] = data["ProductSKU"]
    else:
        raise DeserializationError("CreateLicenseRequest.product_sku required")
    if "Issuer" in data:
        import aws_sdk_license_manager.types.issuer

        out["issuer"] = aws_sdk_license_manager.types.issuer.deserialize_aws_json_1_1(
            data["Issuer"]
        )
    else:
        raise DeserializationError("CreateLicenseRequest.issuer required")
    if "HomeRegion" in data:
        out["home_region"] = data["HomeRegion"]
    else:
        raise DeserializationError("CreateLicenseRequest.home_region required")
    if "Validity" in data:
        import aws_sdk_license_manager.types.datetime_range

        out["validity"] = (
            aws_sdk_license_manager.types.datetime_range.deserialize_aws_json_1_1(
                data["Validity"]
            )
        )
    else:
        raise DeserializationError("CreateLicenseRequest.validity required")
    if "Entitlements" in data:
        import aws_sdk_license_manager.types.entitlement_list

        out["entitlements"] = (
            aws_sdk_license_manager.types.entitlement_list.deserialize_aws_json_1_1(
                data["Entitlements"]
            )
        )
    else:
        raise DeserializationError("CreateLicenseRequest.entitlements required")
    if "Beneficiary" in data:
        out["beneficiary"] = data["Beneficiary"]
    else:
        raise DeserializationError("CreateLicenseRequest.beneficiary required")
    if "ConsumptionConfiguration" in data:
        import aws_sdk_license_manager.types.consumption_configuration

        out["consumption_configuration"] = (
            aws_sdk_license_manager.types.consumption_configuration.deserialize_aws_json_1_1(
                data["ConsumptionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLicenseRequest.consumption_configuration required"
        )
    if "LicenseMetadata" in data:
        import aws_sdk_license_manager.types.metadata_list

        out["license_metadata"] = (
            aws_sdk_license_manager.types.metadata_list.deserialize_aws_json_1_1(
                data["LicenseMetadata"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("CreateLicenseRequest.client_token required")
    if "Tags" in data:
        import aws_sdk_license_manager.types.tag_list

        out["tags"] = aws_sdk_license_manager.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
