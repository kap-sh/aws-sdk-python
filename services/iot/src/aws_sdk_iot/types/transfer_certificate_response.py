"""Generated from Smithy shape ``com.amazonaws.iot#TransferCertificateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_arn


class TransferCertificateResponse(TypedDict):
    transferred_certificate_arn: NotRequired[
        "aws_sdk_iot.types.certificate_arn.CertificateArn"
    ]
    """<p>The ARN of the certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransferCertificateResponse) -> dict:
    out: dict = {}
    if "transferred_certificate_arn" in value:
        out["transferredCertificateArn"] = value["transferred_certificate_arn"]
    return out


def deserialize_json(data: dict) -> TransferCertificateResponse:
    out: TransferCertificateResponse = {}  # type: ignore[typeddict-item]
    if "transferredCertificateArn" in data:
        out["transferred_certificate_arn"] = data["transferredCertificateArn"]
    return out
