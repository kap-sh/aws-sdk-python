"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetServiceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.auth_type
    import aws_sdk_vpc_lattice.types.certificate_arn
    import aws_sdk_vpc_lattice.types.dns_entry
    import aws_sdk_vpc_lattice.types.failure_code
    import aws_sdk_vpc_lattice.types.failure_message
    import aws_sdk_vpc_lattice.types.service_arn
    import aws_sdk_vpc_lattice.types.service_custom_domain_name
    import aws_sdk_vpc_lattice.types.service_id
    import aws_sdk_vpc_lattice.types.service_name
    import aws_sdk_vpc_lattice.types.service_status
    import aws_sdk_vpc_lattice.types.timestamp


class GetServiceResponse(TypedDict, closed=True):
    id: NotRequired["aws_sdk_vpc_lattice.types.service_id.ServiceId"]
    """<p>The ID of the service.</p>"""
    name: NotRequired["aws_sdk_vpc_lattice.types.service_name.ServiceName"]
    """<p>The name of the service.</p>"""
    arn: NotRequired["aws_sdk_vpc_lattice.types.service_arn.ServiceArn"]
    """<p>The Amazon Resource Name (ARN) of the service.</p>"""
    created_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the service was created, in ISO-8601 format.</p>"""
    last_updated_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the service was last updated, in ISO-8601 format.</p>"""
    dns_entry: NotRequired["aws_sdk_vpc_lattice.types.dns_entry.DnsEntry"]
    """<p>The DNS name of the service.</p>"""
    custom_domain_name: NotRequired[
        "aws_sdk_vpc_lattice.types.service_custom_domain_name.ServiceCustomDomainName"
    ]
    """<p>The custom domain name of the service.</p>"""
    certificate_arn: NotRequired[
        "aws_sdk_vpc_lattice.types.certificate_arn.CertificateArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the certificate.</p>"""
    status: NotRequired["aws_sdk_vpc_lattice.types.service_status.ServiceStatus"]
    """<p>The status of the service.</p>"""
    auth_type: NotRequired["aws_sdk_vpc_lattice.types.auth_type.AuthType"]
    """<p>The type of IAM policy.</p>"""
    failure_code: NotRequired["aws_sdk_vpc_lattice.types.failure_code.FailureCode"]
    """<p>The failure code.</p>"""
    failure_message: NotRequired[
        "aws_sdk_vpc_lattice.types.failure_message.FailureMessage"
    ]
    """<p>The failure message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["createdAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["lastUpdatedAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "dns_entry" in value:
        import aws_sdk_vpc_lattice.types.dns_entry

        out["dnsEntry"] = aws_sdk_vpc_lattice.types.dns_entry.serialize_json(
            value["dns_entry"]
        )
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "auth_type" in value:
        out["authType"] = value["auth_type"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    return out


def deserialize_json(data: dict) -> GetServiceResponse:
    out: GetServiceResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["created_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["last_updated_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "dnsEntry" in data:
        import aws_sdk_vpc_lattice.types.dns_entry

        out["dns_entry"] = aws_sdk_vpc_lattice.types.dns_entry.deserialize_json(
            data["dnsEntry"]
        )
    if "customDomainName" in data:
        out["custom_domain_name"] = data["customDomainName"]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "status" in data:
        out["status"] = data["status"]
    if "authType" in data:
        out["auth_type"] = data["authType"]
    if "failureCode" in data:
        out["failure_code"] = data["failureCode"]
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    return out
