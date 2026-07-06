"""Generated from Smithy shape ``com.amazonaws.rtbfabric#DisassociateCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.acm_certificate_arn
    import aws_sdk_rtbfabric.types.gateway_id


class DisassociateCertificateRequest(TypedDict, closed=True):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    acm_certificate_arn: "aws_sdk_rtbfabric.types.acm_certificate_arn.AcmCertificateArn"
    """<p>The Amazon Resource Name (ARN) of the ACM certificate to disassociate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateCertificateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateCertificateRequest:
    out: DisassociateCertificateRequest = {}  # type: ignore[typeddict-item]
    return out
