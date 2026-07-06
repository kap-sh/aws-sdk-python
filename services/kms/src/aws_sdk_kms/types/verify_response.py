"""Generated from Smithy shape ``com.amazonaws.kms#VerifyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kms.types.boolean_type
    import aws_sdk_kms.types.key_id_type
    import aws_sdk_kms.types.signing_algorithm_spec


class VerifyResponse(TypedDict, closed=True):
    key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    r"""<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">key ARN</a>) of the asymmetric KMS key that was used to verify the signature.</p>"""
    signature_valid: "aws_sdk_kms.types.boolean_type.BooleanType"
    """<p>A Boolean value that indicates whether the signature was verified. A value of <code>True</code> indicates that the <code>Signature</code> was produced by signing the <code>Message</code> with the specified <code>KeyID</code> and <code>SigningAlgorithm.</code> If the signature is not verified, the <code>Verify</code> operation fails with a <code>KMSInvalidSignatureException</code> exception. </p>"""
    signing_algorithm: NotRequired[
        "aws_sdk_kms.types.signing_algorithm_spec.SigningAlgorithmSpec"
    ]
    """<p>The signing algorithm that was used to verify the signature.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VerifyResponse) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    out["SignatureValid"] = value.get("signature_valid", False)
    if "signing_algorithm" in value:
        import aws_sdk_kms.types.signing_algorithm_spec

        out["SigningAlgorithm"] = (
            aws_sdk_kms.types.signing_algorithm_spec.serialize_aws_json_1_1(
                value["signing_algorithm"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VerifyResponse:
    out: VerifyResponse = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "SignatureValid" in data:
        out["signature_valid"] = data["SignatureValid"]
    else:
        out["signature_valid"] = False
    if "SigningAlgorithm" in data:
        import aws_sdk_kms.types.signing_algorithm_spec

        out["signing_algorithm"] = (
            aws_sdk_kms.types.signing_algorithm_spec.deserialize_aws_json_1_1(
                data["SigningAlgorithm"]
            )
        )
    return out
