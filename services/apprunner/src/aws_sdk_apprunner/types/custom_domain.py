"""Generated from Smithy shape ``com.amazonaws.apprunner#CustomDomain``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.certificate_validation_record_list
    import aws_sdk_apprunner.types.custom_domain_association_status
    import aws_sdk_apprunner.types.domain_name
    import aws_sdk_apprunner.types.nullable_boolean


class CustomDomain(TypedDict):
    domain_name: "aws_sdk_apprunner.types.domain_name.DomainName"
    """<p>An associated custom domain endpoint. It can be a root domain (for example, <code>example.com</code>), a subdomain (for example, <code>login.example.com</code> or <code>admin.login.example.com</code>), or a wildcard (for example, <code>*.example.com</code>).</p>"""
    enable_www_subdomain: "aws_sdk_apprunner.types.nullable_boolean.NullableBoolean"
    """<p>When <code>true</code>, the subdomain <code>www.<i>DomainName</i> </code> is associated with the App Runner service in addition to the base domain.</p>"""
    certificate_validation_records: NotRequired[
        "aws_sdk_apprunner.types.certificate_validation_record_list.CertificateValidationRecordList"
    ]
    """<p>A list of certificate CNAME records that's used for this domain name.</p>"""
    status: "aws_sdk_apprunner.types.custom_domain_association_status.CustomDomainAssociationStatus"
    """<p>The current state of the domain name association.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomDomain) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["EnableWWWSubdomain"] = value["enable_www_subdomain"]
    if "certificate_validation_records" in value:
        import aws_sdk_apprunner.types.certificate_validation_record_list

        out["CertificateValidationRecords"] = (
            aws_sdk_apprunner.types.certificate_validation_record_list.serialize_aws_json_1_0(
                value["certificate_validation_records"]
            )
        )
    import aws_sdk_apprunner.types.custom_domain_association_status

    out["Status"] = (
        aws_sdk_apprunner.types.custom_domain_association_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomDomain:
    out: CustomDomain = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("CustomDomain.domain_name required")
    if "EnableWWWSubdomain" in data:
        out["enable_www_subdomain"] = data["EnableWWWSubdomain"]
    else:
        raise DeserializationError("CustomDomain.enable_www_subdomain required")
    if "CertificateValidationRecords" in data:
        import aws_sdk_apprunner.types.certificate_validation_record_list

        out["certificate_validation_records"] = (
            aws_sdk_apprunner.types.certificate_validation_record_list.deserialize_aws_json_1_0(
                data["CertificateValidationRecords"]
            )
        )
    if "Status" in data:
        import aws_sdk_apprunner.types.custom_domain_association_status

        out["status"] = (
            aws_sdk_apprunner.types.custom_domain_association_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("CustomDomain.status required")
    return out
