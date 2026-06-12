"""Generated from Smithy shape ``com.amazonaws.iot#DeleteCertificateProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_provider_name


class DeleteCertificateProviderRequest(TypedDict):
    certificate_provider_name: (
        "aws_sdk_iot.types.certificate_provider_name.CertificateProviderName"
    )
    """<p>The name of the certificate provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCertificateProviderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCertificateProviderRequest:
    out: DeleteCertificateProviderRequest = {}  # type: ignore[typeddict-item]
    return out
