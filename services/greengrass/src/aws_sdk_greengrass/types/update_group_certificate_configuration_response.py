"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateGroupCertificateConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class UpdateGroupCertificateConfigurationResponse(TypedDict):
    certificate_authority_expiry_in_milliseconds: NotRequired[
        "aws_sdk_greengrass.types.__string.__string"
    ]
    """The amount of time remaining before the certificate authority expires, in milliseconds."""
    certificate_expiry_in_milliseconds: NotRequired[
        "aws_sdk_greengrass.types.__string.__string"
    ]
    """The amount of time remaining before the certificate expires, in milliseconds."""
    group_id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ID of the group certificate configuration."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGroupCertificateConfigurationResponse) -> dict:
    out: dict = {}
    if "certificate_authority_expiry_in_milliseconds" in value:
        out["CertificateAuthorityExpiryInMilliseconds"] = value[
            "certificate_authority_expiry_in_milliseconds"
        ]
    if "certificate_expiry_in_milliseconds" in value:
        out["CertificateExpiryInMilliseconds"] = value[
            "certificate_expiry_in_milliseconds"
        ]
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> UpdateGroupCertificateConfigurationResponse:
    out: UpdateGroupCertificateConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "CertificateAuthorityExpiryInMilliseconds" in data:
        out["certificate_authority_expiry_in_milliseconds"] = data[
            "CertificateAuthorityExpiryInMilliseconds"
        ]
    if "CertificateExpiryInMilliseconds" in data:
        out["certificate_expiry_in_milliseconds"] = data[
            "CertificateExpiryInMilliseconds"
        ]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    return out
