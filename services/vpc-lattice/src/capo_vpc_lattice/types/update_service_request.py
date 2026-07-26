"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.auth_type
    import capo_vpc_lattice.types.certificate_arn
    import capo_vpc_lattice.types.service_identifier


class UpdateServiceRequest(TypedDict, closed=True):
    service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    certificate_arn: NotRequired[
        "capo_vpc_lattice.types.certificate_arn.CertificateArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the certificate.</p>"""
    auth_type: NotRequired["capo_vpc_lattice.types.auth_type.AuthType"]
    """<p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceRequest) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "auth_type" in value:
        out["authType"] = value["auth_type"]
    return out


def deserialize_json(data: dict) -> UpdateServiceRequest:
    out: UpdateServiceRequest = {}  # type: ignore[typeddict-item]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "authType" in data:
        out["auth_type"] = data["authType"]
    return out
