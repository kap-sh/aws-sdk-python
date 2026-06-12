"""Generated from Smithy shape ``com.amazonaws.iot#CertificateProviderSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_provider_arn
    import aws_sdk_iot.types.certificate_provider_name


class CertificateProviderSummary(TypedDict):
    certificate_provider_name: NotRequired[
        "aws_sdk_iot.types.certificate_provider_name.CertificateProviderName"
    ]
    """<p>The name of the certificate provider.</p>"""
    certificate_provider_arn: NotRequired[
        "aws_sdk_iot.types.certificate_provider_arn.CertificateProviderArn"
    ]
    """<p>The ARN of the certificate provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CertificateProviderSummary) -> dict:
    out: dict = {}
    if "certificate_provider_name" in value:
        out["certificateProviderName"] = value["certificate_provider_name"]
    if "certificate_provider_arn" in value:
        out["certificateProviderArn"] = value["certificate_provider_arn"]
    return out


def deserialize_json(data: dict) -> CertificateProviderSummary:
    out: CertificateProviderSummary = {}  # type: ignore[typeddict-item]
    if "certificateProviderName" in data:
        out["certificate_provider_name"] = data["certificateProviderName"]
    if "certificateProviderArn" in data:
        out["certificate_provider_arn"] = data["certificateProviderArn"]
    return out
