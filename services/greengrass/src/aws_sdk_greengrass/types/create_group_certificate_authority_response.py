"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateGroupCertificateAuthorityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class CreateGroupCertificateAuthorityResponse(TypedDict, closed=True):
    group_certificate_authority_arn: NotRequired[
        "aws_sdk_greengrass.types.__string.__string"
    ]
    """The ARN of the group certificate authority."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupCertificateAuthorityResponse) -> dict:
    out: dict = {}
    if "group_certificate_authority_arn" in value:
        out["GroupCertificateAuthorityArn"] = value["group_certificate_authority_arn"]
    return out


def deserialize_json(data: dict) -> CreateGroupCertificateAuthorityResponse:
    out: CreateGroupCertificateAuthorityResponse = {}  # type: ignore[typeddict-item]
    if "GroupCertificateAuthorityArn" in data:
        out["group_certificate_authority_arn"] = data["GroupCertificateAuthorityArn"]
    return out
