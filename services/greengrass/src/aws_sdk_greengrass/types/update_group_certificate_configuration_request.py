"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateGroupCertificateConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class UpdateGroupCertificateConfigurationRequest(TypedDict):
    certificate_expiry_in_milliseconds: NotRequired[
        "aws_sdk_greengrass.types.__string.__string"
    ]
    """The amount of time remaining before the certificate expires, in milliseconds."""
    group_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the Greengrass group."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGroupCertificateConfigurationRequest) -> dict:
    out: dict = {}
    if "certificate_expiry_in_milliseconds" in value:
        out["CertificateExpiryInMilliseconds"] = value[
            "certificate_expiry_in_milliseconds"
        ]
    return out


def deserialize_json(data: dict) -> UpdateGroupCertificateConfigurationRequest:
    out: UpdateGroupCertificateConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "CertificateExpiryInMilliseconds" in data:
        out["certificate_expiry_in_milliseconds"] = data[
            "CertificateExpiryInMilliseconds"
        ]
    return out
