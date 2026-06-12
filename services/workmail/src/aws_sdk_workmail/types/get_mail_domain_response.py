"""Generated from Smithy shape ``com.amazonaws.workmail#GetMailDomainResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.boolean
    import aws_sdk_workmail.types.dns_record_verification_status
    import aws_sdk_workmail.types.dns_records


class GetMailDomainResponse(TypedDict):
    records: NotRequired["aws_sdk_workmail.types.dns_records.DnsRecords"]
    """<p>A list of the DNS records that WorkMail recommends adding in your DNS provider for the best user experience. The records configure your domain with DMARC, SPF, DKIM, and direct incoming email traffic to SES. See admin guide for more details.</p>"""
    is_test_domain: "aws_sdk_workmail.types.boolean.Boolean"
    """<p>Specifies whether the domain is a test domain provided by WorkMail, or a custom domain.</p>"""
    is_default: "aws_sdk_workmail.types.boolean.Boolean"
    """<p>Specifies whether the domain is the default domain for your organization.</p>"""
    ownership_verification_status: NotRequired[
        "aws_sdk_workmail.types.dns_record_verification_status.DnsRecordVerificationStatus"
    ]
    """<p> Indicates the status of the domain ownership verification.</p>"""
    dkim_verification_status: NotRequired[
        "aws_sdk_workmail.types.dns_record_verification_status.DnsRecordVerificationStatus"
    ]
    """<p>Indicates the status of a DKIM verification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMailDomainResponse) -> dict:
    out: dict = {}
    if "records" in value:
        import aws_sdk_workmail.types.dns_records

        out["Records"] = aws_sdk_workmail.types.dns_records.serialize_aws_json_1_1(
            value["records"]
        )
    out["IsTestDomain"] = value.get("is_test_domain", False)
    out["IsDefault"] = value.get("is_default", False)
    if "ownership_verification_status" in value:
        import aws_sdk_workmail.types.dns_record_verification_status

        out["OwnershipVerificationStatus"] = (
            aws_sdk_workmail.types.dns_record_verification_status.serialize_aws_json_1_1(
                value["ownership_verification_status"]
            )
        )
    if "dkim_verification_status" in value:
        import aws_sdk_workmail.types.dns_record_verification_status

        out["DkimVerificationStatus"] = (
            aws_sdk_workmail.types.dns_record_verification_status.serialize_aws_json_1_1(
                value["dkim_verification_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMailDomainResponse:
    out: GetMailDomainResponse = {}  # type: ignore[typeddict-item]
    if "Records" in data:
        import aws_sdk_workmail.types.dns_records

        out["records"] = aws_sdk_workmail.types.dns_records.deserialize_aws_json_1_1(
            data["Records"]
        )
    if "IsTestDomain" in data:
        out["is_test_domain"] = data["IsTestDomain"]
    else:
        out["is_test_domain"] = False
    if "IsDefault" in data:
        out["is_default"] = data["IsDefault"]
    else:
        out["is_default"] = False
    if "OwnershipVerificationStatus" in data:
        import aws_sdk_workmail.types.dns_record_verification_status

        out["ownership_verification_status"] = (
            aws_sdk_workmail.types.dns_record_verification_status.deserialize_aws_json_1_1(
                data["OwnershipVerificationStatus"]
            )
        )
    if "DkimVerificationStatus" in data:
        import aws_sdk_workmail.types.dns_record_verification_status

        out["dkim_verification_status"] = (
            aws_sdk_workmail.types.dns_record_verification_status.deserialize_aws_json_1_1(
                data["DkimVerificationStatus"]
            )
        )
    return out
