"""Generated from Smithy shape ``com.amazonaws.acm#CertificateSearchResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.arn
    import capo_acm.types.certificate_metadata
    import capo_acm.types.x509_attributes


class CertificateSearchResult(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_acm.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the certificate.</p>"""
    x509_attributes: NotRequired["capo_acm.types.x509_attributes.X509Attributes"]
    """<p>X.509 certificate attributes such as subject, issuer, and validity period.</p>"""
    certificate_metadata: NotRequired[
        "capo_acm.types.certificate_metadata.CertificateMetadata"
    ]
    """<p>ACM-specific metadata about the certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateSearchResult) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "x509_attributes" in value:
        import capo_acm.types.x509_attributes

        out["X509Attributes"] = capo_acm.types.x509_attributes.serialize_aws_json_1_1(
            value["x509_attributes"]
        )
    if "certificate_metadata" in value:
        import capo_acm.types.certificate_metadata

        out["CertificateMetadata"] = (
            capo_acm.types.certificate_metadata.serialize_aws_json_1_1(
                value["certificate_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateSearchResult:
    out: CertificateSearchResult = {}  # type: ignore[typeddict-item]
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    if "X509Attributes" in data:
        import capo_acm.types.x509_attributes

        out["x509_attributes"] = (
            capo_acm.types.x509_attributes.deserialize_aws_json_1_1(
                data["X509Attributes"]
            )
        )
    if "CertificateMetadata" in data:
        import capo_acm.types.certificate_metadata

        out["certificate_metadata"] = (
            capo_acm.types.certificate_metadata.deserialize_aws_json_1_1(
                data["CertificateMetadata"]
            )
        )
    return out
