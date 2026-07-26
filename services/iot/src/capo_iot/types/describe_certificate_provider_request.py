"""Generated from Smithy shape ``com.amazonaws.iot#DescribeCertificateProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.certificate_provider_name


class DescribeCertificateProviderRequest(TypedDict, closed=True):
    certificate_provider_name: (
        "capo_iot.types.certificate_provider_name.CertificateProviderName"
    )
    """<p>The name of the certificate provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCertificateProviderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeCertificateProviderRequest:
    out: DescribeCertificateProviderRequest = {}  # type: ignore[typeddict-item]
    return out
