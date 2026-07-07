"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GetCertificateAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.acm_certificate_arn
    import aws_sdk_rtbfabric.types.gateway_id


class GetCertificateAssociationRequest(TypedDict, closed=True):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    acm_certificate_arn: "aws_sdk_rtbfabric.types.acm_certificate_arn.AcmCertificateArn"
    """<p>The Amazon Resource Name (ARN) of the ACM certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCertificateAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCertificateAssociationRequest:
    out: GetCertificateAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
