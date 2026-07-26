"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GetCertificateAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_rtbfabric.types.acm_certificate_arn
    import capo_rtbfabric.types.certificate_association_status
    import capo_rtbfabric.types.gateway_id


class GetCertificateAssociationResponse(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    acm_certificate_arn: "capo_rtbfabric.types.acm_certificate_arn.AcmCertificateArn"
    """<p>The Amazon Resource Name (ARN) of the ACM certificate.</p>"""
    status: "capo_rtbfabric.types.certificate_association_status.CertificateAssociationStatus"
    """<p>The status of the certificate association.</p>"""
    associated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the certificate was associated.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the certificate association was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCertificateAssociationResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["acmCertificateArn"] = value["acm_certificate_arn"]
    import capo_rtbfabric.types.certificate_association_status

    out["status"] = capo_rtbfabric.types.certificate_association_status.serialize_json(
        value["status"]
    )
    if "associated_at" in value:
        import capo_rtbfabric.types._prelude.timestamp

        out["associatedAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
            value["associated_at"]
        )
    if "updated_at" in value:
        import capo_rtbfabric.types._prelude.timestamp

        out["updatedAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetCertificateAssociationResponse:
    out: GetCertificateAssociationResponse = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError(
            "GetCertificateAssociationResponse.gateway_id required"
        )
    if "acmCertificateArn" in data:
        out["acm_certificate_arn"] = data["acmCertificateArn"]
    else:
        raise DeserializationError(
            "GetCertificateAssociationResponse.acm_certificate_arn required"
        )
    if "status" in data:
        import capo_rtbfabric.types.certificate_association_status

        out["status"] = (
            capo_rtbfabric.types.certificate_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetCertificateAssociationResponse.status required")
    if "associatedAt" in data:
        import capo_rtbfabric.types._prelude.timestamp

        out["associated_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["associatedAt"]
        )
    if "updatedAt" in data:
        import capo_rtbfabric.types._prelude.timestamp

        out["updated_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
