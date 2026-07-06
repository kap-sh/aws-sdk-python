"""Generated from Smithy shape ``com.amazonaws.iot#CustomCodeSigning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.code_signing_certificate_chain
    import aws_sdk_iot.types.code_signing_signature
    import aws_sdk_iot.types.hash_algorithm
    import aws_sdk_iot.types.signature_algorithm


class CustomCodeSigning(TypedDict, closed=True):
    signature: NotRequired[
        "aws_sdk_iot.types.code_signing_signature.CodeSigningSignature"
    ]
    """<p>The signature for the file.</p>"""
    certificate_chain: NotRequired[
        "aws_sdk_iot.types.code_signing_certificate_chain.CodeSigningCertificateChain"
    ]
    """<p>The certificate chain.</p>"""
    hash_algorithm: NotRequired["aws_sdk_iot.types.hash_algorithm.HashAlgorithm"]
    """<p>The hash algorithm used to code sign the file. You can use a string as the algorithm name if the target over-the-air (OTA) update devices are able to verify the signature that was generated using the same signature algorithm. For example, FreeRTOS uses <code>SHA256</code> or <code>SHA1</code>, so you can pass either of them based on which was used for generating the signature.</p>"""
    signature_algorithm: NotRequired[
        "aws_sdk_iot.types.signature_algorithm.SignatureAlgorithm"
    ]
    """<p>The signature algorithm used to code sign the file. You can use a string as the algorithm name if the target over-the-air (OTA) update devices are able to verify the signature that was generated using the same signature algorithm. For example, FreeRTOS uses <code>ECDSA</code> or <code>RSA</code>, so you can pass either of them based on which was used for generating the signature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomCodeSigning) -> dict:
    out: dict = {}
    if "signature" in value:
        import aws_sdk_iot.types.code_signing_signature

        out["signature"] = aws_sdk_iot.types.code_signing_signature.serialize_json(
            value["signature"]
        )
    if "certificate_chain" in value:
        import aws_sdk_iot.types.code_signing_certificate_chain

        out["certificateChain"] = (
            aws_sdk_iot.types.code_signing_certificate_chain.serialize_json(
                value["certificate_chain"]
            )
        )
    if "hash_algorithm" in value:
        out["hashAlgorithm"] = value["hash_algorithm"]
    if "signature_algorithm" in value:
        out["signatureAlgorithm"] = value["signature_algorithm"]
    return out


def deserialize_json(data: dict) -> CustomCodeSigning:
    out: CustomCodeSigning = {}  # type: ignore[typeddict-item]
    if "signature" in data:
        import aws_sdk_iot.types.code_signing_signature

        out["signature"] = aws_sdk_iot.types.code_signing_signature.deserialize_json(
            data["signature"]
        )
    if "certificateChain" in data:
        import aws_sdk_iot.types.code_signing_certificate_chain

        out["certificate_chain"] = (
            aws_sdk_iot.types.code_signing_certificate_chain.deserialize_json(
                data["certificateChain"]
            )
        )
    if "hashAlgorithm" in data:
        out["hash_algorithm"] = data["hashAlgorithm"]
    if "signatureAlgorithm" in data:
        out["signature_algorithm"] = data["signatureAlgorithm"]
    return out
