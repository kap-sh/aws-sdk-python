"""Generated from Smithy shape ``com.amazonaws.iot#DescribeCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.certificate_id


class DescribeCertificateRequest(TypedDict, closed=True):
    certificate_id: "capo_iot.types.certificate_id.CertificateId"
    """<p>The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCertificateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeCertificateRequest:
    out: DescribeCertificateRequest = {}  # type: ignore[typeddict-item]
    return out
