"""Generated from Smithy shape ``com.amazonaws.kms#VerifyResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.boolean_type
    import awd_sdk_kms.types.key_id_type
    import awd_sdk_kms.types.signing_algorithm_spec


class VerifyResponse(TypedDict):
    key_id: NotRequired["awd_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">key ARN</a>) of the asymmetric KMS key that was used to verify the signature.</p>"""
    signature_valid: "awd_sdk_kms.types.boolean_type.BooleanType"
    """<p>A Boolean value that indicates whether the signature was verified. A value of <code>True</code> indicates that the <code>Signature</code> was produced by signing the <code>Message</code> with the specified <code>KeyID</code> and <code>SigningAlgorithm.</code> If the signature is not verified, the <code>Verify</code> operation fails with a <code>KMSInvalidSignatureException</code> exception. </p>"""
    signing_algorithm: NotRequired[
        "awd_sdk_kms.types.signing_algorithm_spec.SigningAlgorithmSpec"
    ]
    """<p>The signing algorithm that was used to verify the signature.</p>"""
