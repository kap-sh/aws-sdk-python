"""Generated from Smithy shape ``com.amazonaws.greengrass#GetGroupCertificateAuthorityRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class GetGroupCertificateAuthorityRequest(TypedDict):
    certificate_authority_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the certificate authority."""
    group_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the Greengrass group."""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupCertificateAuthorityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGroupCertificateAuthorityRequest:
    out: GetGroupCertificateAuthorityRequest = {}  # type: ignore[typeddict-item]
    return out
