"""Generated from Smithy shape ``com.amazonaws.iot#DescribeCACertificateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_id


class DescribeCACertificateRequest(TypedDict):
    certificate_id: "aws_sdk_iot.types.certificate_id.CertificateId"
    """<p>The CA certificate identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCACertificateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeCACertificateRequest:
    out: DescribeCACertificateRequest = {}  # type: ignore[typeddict-item]
    return out
