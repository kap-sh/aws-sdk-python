"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateServiceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.auth_type
    import aws_sdk_vpc_lattice.types.certificate_arn
    import aws_sdk_vpc_lattice.types.dns_entry
    import aws_sdk_vpc_lattice.types.service_arn
    import aws_sdk_vpc_lattice.types.service_custom_domain_name
    import aws_sdk_vpc_lattice.types.service_id
    import aws_sdk_vpc_lattice.types.service_name
    import aws_sdk_vpc_lattice.types.service_status


class CreateServiceResponse(TypedDict, closed=True):
    id: NotRequired["aws_sdk_vpc_lattice.types.service_id.ServiceId"]
    """<p>The ID of the service.</p>"""
    arn: NotRequired["aws_sdk_vpc_lattice.types.service_arn.ServiceArn"]
    """<p>The Amazon Resource Name (ARN) of the service.</p>"""
    name: NotRequired["aws_sdk_vpc_lattice.types.service_name.ServiceName"]
    """<p>The name of the service.</p>"""
    custom_domain_name: NotRequired[
        "aws_sdk_vpc_lattice.types.service_custom_domain_name.ServiceCustomDomainName"
    ]
    """<p>The custom domain name of the service.</p>"""
    certificate_arn: NotRequired[
        "aws_sdk_vpc_lattice.types.certificate_arn.CertificateArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the certificate.</p>"""
    status: NotRequired["aws_sdk_vpc_lattice.types.service_status.ServiceStatus"]
    """<p>The status. If the status is <code>CREATE_FAILED</code>, you must delete and recreate the service.</p>"""
    auth_type: NotRequired["aws_sdk_vpc_lattice.types.auth_type.AuthType"]
    """<p>The type of IAM policy.</p>"""
    dns_entry: NotRequired["aws_sdk_vpc_lattice.types.dns_entry.DnsEntry"]
    """<p>The public DNS name of the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "auth_type" in value:
        out["authType"] = value["auth_type"]
    if "dns_entry" in value:
        import aws_sdk_vpc_lattice.types.dns_entry

        out["dnsEntry"] = aws_sdk_vpc_lattice.types.dns_entry.serialize_json(
            value["dns_entry"]
        )
    return out


def deserialize_json(data: dict) -> CreateServiceResponse:
    out: CreateServiceResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "customDomainName" in data:
        out["custom_domain_name"] = data["customDomainName"]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "status" in data:
        out["status"] = data["status"]
    if "authType" in data:
        out["auth_type"] = data["authType"]
    if "dnsEntry" in data:
        import aws_sdk_vpc_lattice.types.dns_entry

        out["dns_entry"] = aws_sdk_vpc_lattice.types.dns_entry.deserialize_json(
            data["dnsEntry"]
        )
    return out
