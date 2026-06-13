"""Generated from Smithy shape ``com.amazonaws.rtbfabric#DisassociateCertificateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.acm_certificate_arn
    import aws_sdk_rtbfabric.types.certificate_association_status
    import aws_sdk_rtbfabric.types.gateway_id


class DisassociateCertificateResponse(TypedDict):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    acm_certificate_arn: "aws_sdk_rtbfabric.types.acm_certificate_arn.AcmCertificateArn"
    """<p>The Amazon Resource Name (ARN) of the ACM certificate.</p>"""
    status: "aws_sdk_rtbfabric.types.certificate_association_status.CertificateAssociationStatus"
    """<p>The status of the certificate association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateCertificateResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["acmCertificateArn"] = value["acm_certificate_arn"]
    import aws_sdk_rtbfabric.types.certificate_association_status

    out["status"] = (
        aws_sdk_rtbfabric.types.certificate_association_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DisassociateCertificateResponse:
    out: DisassociateCertificateResponse = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError(
            "DisassociateCertificateResponse.gateway_id required"
        )
    if "acmCertificateArn" in data:
        out["acm_certificate_arn"] = data["acmCertificateArn"]
    else:
        raise DeserializationError(
            "DisassociateCertificateResponse.acm_certificate_arn required"
        )
    if "status" in data:
        import aws_sdk_rtbfabric.types.certificate_association_status

        out["status"] = (
            aws_sdk_rtbfabric.types.certificate_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DisassociateCertificateResponse.status required")
    return out
