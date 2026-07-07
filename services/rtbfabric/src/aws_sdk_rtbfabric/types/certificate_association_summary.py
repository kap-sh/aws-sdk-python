"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CertificateAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_rtbfabric.types.acm_certificate_arn
    import aws_sdk_rtbfabric.types.certificate_association_status


class CertificateAssociationSummary(TypedDict, closed=True):
    acm_certificate_arn: "aws_sdk_rtbfabric.types.acm_certificate_arn.AcmCertificateArn"
    """<p>The Amazon Resource Name (ARN) of the ACM certificate.</p>"""
    status: "aws_sdk_rtbfabric.types.certificate_association_status.CertificateAssociationStatus"
    """<p>The status of the certificate association.</p>"""
    associated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the certificate was associated.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the certificate association was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CertificateAssociationSummary) -> dict:
    out: dict = {}
    out["acmCertificateArn"] = value["acm_certificate_arn"]
    import aws_sdk_rtbfabric.types.certificate_association_status

    out["status"] = (
        aws_sdk_rtbfabric.types.certificate_association_status.serialize_json(
            value["status"]
        )
    )
    if "associated_at" in value:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["associatedAt"] = aws_sdk_rtbfabric.types._prelude.timestamp.serialize_json(
            value["associated_at"]
        )
    if "updated_at" in value:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["updatedAt"] = aws_sdk_rtbfabric.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> CertificateAssociationSummary:
    out: CertificateAssociationSummary = {}  # type: ignore[typeddict-item]
    if "acmCertificateArn" in data:
        out["acm_certificate_arn"] = data["acmCertificateArn"]
    else:
        raise DeserializationError(
            "CertificateAssociationSummary.acm_certificate_arn required"
        )
    if "status" in data:
        import aws_sdk_rtbfabric.types.certificate_association_status

        out["status"] = (
            aws_sdk_rtbfabric.types.certificate_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CertificateAssociationSummary.status required")
    if "associatedAt" in data:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["associated_at"] = (
            aws_sdk_rtbfabric.types._prelude.timestamp.deserialize_json(
                data["associatedAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["updated_at"] = aws_sdk_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
