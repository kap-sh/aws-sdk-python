"""Generated from Smithy shape ``com.amazonaws.iam#UploadSigningCertificateResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.signing_certificate


class UploadSigningCertificateResponse(TypedDict):
    certificate: "aws_sdk_iam.types.signing_certificate.SigningCertificate"
    """<p>Information about the certificate.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UploadSigningCertificateResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.signing_certificate

    aws_sdk_iam.types.signing_certificate.serialize_query(
        value["certificate"], pairs, f"{prefix}.Certificate"
    )


def deserialize_query(el: Element) -> UploadSigningCertificateResponse:
    out: UploadSigningCertificateResponse = {}  # type: ignore[typeddict-item]
    child_certificate = el.find("Certificate")
    if child_certificate is not None:
        import aws_sdk_iam.types.signing_certificate

        out["certificate"] = aws_sdk_iam.types.signing_certificate.deserialize_query(
            child_certificate
        )
    else:
        raise DeserializationError(
            "UploadSigningCertificateResponse.certificate required"
        )
    return out
