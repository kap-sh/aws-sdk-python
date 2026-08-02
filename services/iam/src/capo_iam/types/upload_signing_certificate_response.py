"""Generated from Smithy shape ``com.amazonaws.iam#UploadSigningCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.signing_certificate


class UploadSigningCertificateResponse(TypedDict, closed=True):
    certificate: "capo_iam.types.signing_certificate.SigningCertificate"
    """<p>Information about the certificate.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UploadSigningCertificateResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.signing_certificate

    capo_iam.types.signing_certificate.serialize_query(
        value["certificate"], pairs, f"{key_prefix}Certificate"
    )


def deserialize_query(el: Element) -> UploadSigningCertificateResponse:
    out: UploadSigningCertificateResponse = {}  # type: ignore[typeddict-item]
    child_certificate = el.find("Certificate")
    if child_certificate is not None:
        import capo_iam.types.signing_certificate

        out["certificate"] = capo_iam.types.signing_certificate.deserialize_query(
            child_certificate
        )
    else:
        raise DeserializationError(
            "UploadSigningCertificateResponse.certificate required"
        )
    return out
