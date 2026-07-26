"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_vpc_lattice.types.auth_type
    import capo_vpc_lattice.types.certificate_arn
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.service_custom_domain_name
    import capo_vpc_lattice.types.service_name
    import capo_vpc_lattice.types.tag_map


class CreateServiceRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_vpc_lattice.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>"""
    name: "capo_vpc_lattice.types.service_name.ServiceName"
    """<p>The name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>"""
    tags: NotRequired["capo_vpc_lattice.types.tag_map.TagMap"]
    """<p>The tags for the service.</p>"""
    custom_domain_name: NotRequired[
        "capo_vpc_lattice.types.service_custom_domain_name.ServiceCustomDomainName"
    ]
    """<p>The custom domain name of the service.</p>"""
    certificate_arn: NotRequired[
        "capo_vpc_lattice.types.certificate_arn.CertificateArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the certificate.</p>"""
    auth_type: NotRequired["capo_vpc_lattice.types.auth_type.AuthType"]
    """<p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    if "tags" in value:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "auth_type" in value:
        out["authType"] = value["auth_type"]
    return out


def deserialize_json(data: dict) -> CreateServiceRequest:
    out: CreateServiceRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateServiceRequest.name required")
    if "tags" in data:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    if "customDomainName" in data:
        out["custom_domain_name"] = data["customDomainName"]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "authType" in data:
        out["auth_type"] = data["authType"]
    return out
