"""Generated from Smithy shape ``com.amazonaws.greengrass#GroupCertificateAuthorityProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class GroupCertificateAuthorityProperties(TypedDict, closed=True):
    group_certificate_authority_arn: NotRequired[
        "capo_greengrass.types.__string.__string"
    ]
    """The ARN of the certificate authority for the group."""
    group_certificate_authority_id: NotRequired[
        "capo_greengrass.types.__string.__string"
    ]
    """The ID of the certificate authority for the group."""


# --- restJson1 ser/de ---
def serialize_json(value: GroupCertificateAuthorityProperties) -> dict:
    out: dict = {}
    if "group_certificate_authority_arn" in value:
        out["GroupCertificateAuthorityArn"] = value["group_certificate_authority_arn"]
    if "group_certificate_authority_id" in value:
        out["GroupCertificateAuthorityId"] = value["group_certificate_authority_id"]
    return out


def deserialize_json(data: dict) -> GroupCertificateAuthorityProperties:
    out: GroupCertificateAuthorityProperties = {}  # type: ignore[typeddict-item]
    if "GroupCertificateAuthorityArn" in data:
        out["group_certificate_authority_arn"] = data["GroupCertificateAuthorityArn"]
    if "GroupCertificateAuthorityId" in data:
        out["group_certificate_authority_id"] = data["GroupCertificateAuthorityId"]
    return out
