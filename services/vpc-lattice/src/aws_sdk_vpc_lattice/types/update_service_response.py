"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateServiceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.auth_type
    import aws_sdk_vpc_lattice.types.certificate_arn
    import aws_sdk_vpc_lattice.types.service_arn
    import aws_sdk_vpc_lattice.types.service_custom_domain_name
    import aws_sdk_vpc_lattice.types.service_id
    import aws_sdk_vpc_lattice.types.service_name


class UpdateServiceResponse(TypedDict, closed=True):
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
    auth_type: NotRequired["aws_sdk_vpc_lattice.types.auth_type.AuthType"]
    """<p>The type of IAM policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceResponse) -> dict:
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
    if "auth_type" in value:
        out["authType"] = value["auth_type"]
    return out


def deserialize_json(data: dict) -> UpdateServiceResponse:
    out: UpdateServiceResponse = {}  # type: ignore[typeddict-item]
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
    if "authType" in data:
        out["auth_type"] = data["authType"]
    return out
