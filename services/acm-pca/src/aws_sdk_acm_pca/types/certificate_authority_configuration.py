"""Generated from Smithy shape ``com.amazonaws.acmpca#CertificateAuthorityConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.asn1_subject
    import aws_sdk_acm_pca.types.csr_extensions
    import aws_sdk_acm_pca.types.key_algorithm
    import aws_sdk_acm_pca.types.signing_algorithm


class CertificateAuthorityConfiguration(TypedDict):
    key_algorithm: "aws_sdk_acm_pca.types.key_algorithm.KeyAlgorithm"
    """<p>Type of the public key algorithm and size, in bits, of the key pair that your CA creates when it issues a certificate. When you create a subordinate CA, you must use a key algorithm supported by the parent CA.</p>"""
    signing_algorithm: "aws_sdk_acm_pca.types.signing_algorithm.SigningAlgorithm"
    """<p>Name of the algorithm your private CA uses to sign certificate requests.</p> <p>This parameter should not be confused with the <code>SigningAlgorithm</code> parameter used to sign certificates when they are issued.</p>"""
    subject: "aws_sdk_acm_pca.types.asn1_subject.ASN1Subject"
    """<p>Structure that contains X.500 distinguished name information for your private CA.</p>"""
    csr_extensions: NotRequired["aws_sdk_acm_pca.types.csr_extensions.CsrExtensions"]
    """<p>Specifies information to be added to the extension section of the certificate signing request (CSR).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateAuthorityConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_acm_pca.types.key_algorithm

    out["KeyAlgorithm"] = aws_sdk_acm_pca.types.key_algorithm.serialize_aws_json_1_1(
        value["key_algorithm"]
    )
    import aws_sdk_acm_pca.types.signing_algorithm

    out["SigningAlgorithm"] = (
        aws_sdk_acm_pca.types.signing_algorithm.serialize_aws_json_1_1(
            value["signing_algorithm"]
        )
    )
    import aws_sdk_acm_pca.types.asn1_subject

    out["Subject"] = aws_sdk_acm_pca.types.asn1_subject.serialize_aws_json_1_1(
        value["subject"]
    )
    if "csr_extensions" in value:
        import aws_sdk_acm_pca.types.csr_extensions

        out["CsrExtensions"] = (
            aws_sdk_acm_pca.types.csr_extensions.serialize_aws_json_1_1(
                value["csr_extensions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateAuthorityConfiguration:
    out: CertificateAuthorityConfiguration = {}  # type: ignore[typeddict-item]
    if "KeyAlgorithm" in data:
        import aws_sdk_acm_pca.types.key_algorithm

        out["key_algorithm"] = (
            aws_sdk_acm_pca.types.key_algorithm.deserialize_aws_json_1_1(
                data["KeyAlgorithm"]
            )
        )
    else:
        raise DeserializationError(
            "CertificateAuthorityConfiguration.key_algorithm required"
        )
    if "SigningAlgorithm" in data:
        import aws_sdk_acm_pca.types.signing_algorithm

        out["signing_algorithm"] = (
            aws_sdk_acm_pca.types.signing_algorithm.deserialize_aws_json_1_1(
                data["SigningAlgorithm"]
            )
        )
    else:
        raise DeserializationError(
            "CertificateAuthorityConfiguration.signing_algorithm required"
        )
    if "Subject" in data:
        import aws_sdk_acm_pca.types.asn1_subject

        out["subject"] = aws_sdk_acm_pca.types.asn1_subject.deserialize_aws_json_1_1(
            data["Subject"]
        )
    else:
        raise DeserializationError("CertificateAuthorityConfiguration.subject required")
    if "CsrExtensions" in data:
        import aws_sdk_acm_pca.types.csr_extensions

        out["csr_extensions"] = (
            aws_sdk_acm_pca.types.csr_extensions.deserialize_aws_json_1_1(
                data["CsrExtensions"]
            )
        )
    return out
