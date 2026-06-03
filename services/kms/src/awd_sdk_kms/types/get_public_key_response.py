"""Generated from Smithy shape ``com.amazonaws.kms#GetPublicKeyResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.customer_master_key_spec
    import awd_sdk_kms.types.encryption_algorithm_spec_list
    import awd_sdk_kms.types.key_agreement_algorithm_spec_list
    import awd_sdk_kms.types.key_id_type
    import awd_sdk_kms.types.key_spec
    import awd_sdk_kms.types.key_usage_type
    import awd_sdk_kms.types.public_key_type
    import awd_sdk_kms.types.signing_algorithm_spec_list


class GetPublicKeyResponse(TypedDict):
    key_id: NotRequired["awd_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">key ARN</a>) of the asymmetric KMS key from which the public key was downloaded.</p>"""
    public_key: NotRequired["awd_sdk_kms.types.public_key_type.PublicKeyType"]
    """<p>The exported public key. </p> <p>The value is a DER-encoded X.509 public key, also known as <code>SubjectPublicKeyInfo</code> (SPKI), as defined in <a href=\"https://tools.ietf.org/html/rfc5280\">RFC 5280</a>. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p> <p></p>"""
    customer_master_key_spec: NotRequired[
        "awd_sdk_kms.types.customer_master_key_spec.CustomerMasterKeySpec"
    ]
    """<p>Instead, use the <code>KeySpec</code> field in the <code>GetPublicKey</code> response.</p> <p>The <code>KeySpec</code> and <code>CustomerMasterKeySpec</code> fields have the same value. We recommend that you use the <code>KeySpec</code> field in your code. However, to avoid breaking changes, KMS supports both fields.</p>"""
    key_spec: NotRequired["awd_sdk_kms.types.key_spec.KeySpec"]
    """<p>The type of the of the public key that was downloaded.</p>"""
    key_usage: NotRequired["awd_sdk_kms.types.key_usage_type.KeyUsageType"]
    """<p>The permitted use of the public key. Valid values for asymmetric key pairs are <code>ENCRYPT_DECRYPT</code>, <code>SIGN_VERIFY</code>, and <code>KEY_AGREEMENT</code>. </p> <p>This information is critical. For example, if a public key with <code>SIGN_VERIFY</code> key usage encrypts data outside of KMS, the ciphertext cannot be decrypted. </p>"""
    encryption_algorithms: NotRequired[
        "awd_sdk_kms.types.encryption_algorithm_spec_list.EncryptionAlgorithmSpecList"
    ]
    """<p>The encryption algorithms that KMS supports for this key. </p> <p>This information is critical. If a public key encrypts data outside of KMS by using an unsupported encryption algorithm, the ciphertext cannot be decrypted. </p> <p>This field appears in the response only when the <code>KeyUsage</code> of the public key is <code>ENCRYPT_DECRYPT</code>.</p>"""
    signing_algorithms: NotRequired[
        "awd_sdk_kms.types.signing_algorithm_spec_list.SigningAlgorithmSpecList"
    ]
    """<p>The signing algorithms that KMS supports for this key.</p> <p>This field appears in the response only when the <code>KeyUsage</code> of the public key is <code>SIGN_VERIFY</code>.</p>"""
    key_agreement_algorithms: NotRequired[
        "awd_sdk_kms.types.key_agreement_algorithm_spec_list.KeyAgreementAlgorithmSpecList"
    ]
    """<p>The key agreement algorithm used to derive a shared secret. This field is present only when the KMS key has a <code>KeyUsage</code> value of <code>KEY_AGREEMENT</code>.</p>"""
