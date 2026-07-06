"""Generated from Smithy shape ``com.amazonaws.greengrass#GetGroupCertificateAuthorityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class GetGroupCertificateAuthorityResponse(TypedDict, closed=True):
    group_certificate_authority_arn: NotRequired[
        "aws_sdk_greengrass.types.__string.__string"
    ]
    """The ARN of the certificate authority for the group."""
    group_certificate_authority_id: NotRequired[
        "aws_sdk_greengrass.types.__string.__string"
    ]
    """The ID of the certificate authority for the group."""
    pem_encoded_certificate: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The PEM encoded certificate for the group."""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupCertificateAuthorityResponse) -> dict:
    out: dict = {}
    if "group_certificate_authority_arn" in value:
        out["GroupCertificateAuthorityArn"] = value["group_certificate_authority_arn"]
    if "group_certificate_authority_id" in value:
        out["GroupCertificateAuthorityId"] = value["group_certificate_authority_id"]
    if "pem_encoded_certificate" in value:
        out["PemEncodedCertificate"] = value["pem_encoded_certificate"]
    return out


def deserialize_json(data: dict) -> GetGroupCertificateAuthorityResponse:
    out: GetGroupCertificateAuthorityResponse = {}  # type: ignore[typeddict-item]
    if "GroupCertificateAuthorityArn" in data:
        out["group_certificate_authority_arn"] = data["GroupCertificateAuthorityArn"]
    if "GroupCertificateAuthorityId" in data:
        out["group_certificate_authority_id"] = data["GroupCertificateAuthorityId"]
    if "PemEncodedCertificate" in data:
        out["pem_encoded_certificate"] = data["PemEncodedCertificate"]
    return out
