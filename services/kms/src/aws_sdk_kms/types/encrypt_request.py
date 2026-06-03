"""Generated from Smithy shape ``com.amazonaws.kms#EncryptRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.encryption_algorithm_spec
    import aws_sdk_kms.types.encryption_context_type
    import aws_sdk_kms.types.grant_token_list
    import aws_sdk_kms.types.key_id_type
    import aws_sdk_kms.types.nullable_boolean_type
    import aws_sdk_kms.types.plaintext_type


class EncryptRequest(TypedDict):
    key_id: "aws_sdk_kms.types.key_id_type.KeyIdType"
    """<p>Identifies the KMS key to use in the encryption operation. The KMS key must have a <code>KeyUsage</code> of <code>ENCRYPT_DECRYPT</code>. To find the <code>KeyUsage</code> of a KMS key, use the <a>DescribeKey</a> operation.</p> <p>To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with <code>\"alias/\"</code>. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Alias name: <code>alias/ExampleAlias</code> </p> </li> <li> <p>Alias ARN: <code>arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>. To get the alias name and alias ARN, use <a>ListAliases</a>.</p>"""
    plaintext: "aws_sdk_kms.types.plaintext_type.PlaintextType"
    """<p>Data to be encrypted.</p>"""
    encryption_context: NotRequired[
        "aws_sdk_kms.types.encryption_context_type.EncryptionContextType"
    ]
    """<p>Specifies the encryption context that will be used to encrypt the data. An encryption context is valid only for <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#cryptographic-operations\">cryptographic operations</a> with a symmetric encryption KMS key. The standard asymmetric encryption algorithms and HMAC algorithms that KMS uses do not support an encryption context. </p> <important> <p>Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important> <p>An <i>encryption context</i> is a collection of non-secret key-value pairs that represent additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is supported only on operations with symmetric encryption KMS keys. On operations with symmetric encryption KMS keys, an encryption context is optional, but it is strongly recommended.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html\">Encryption context</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    grant_tokens: NotRequired["aws_sdk_kms.types.grant_token_list.GrantTokenList"]
    """<p>A list of grant tokens.</p> <p>Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved <i>eventual consistency</i>. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token\">Grant token</a> and <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html\">Using a grant token</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    encryption_algorithm: NotRequired[
        "aws_sdk_kms.types.encryption_algorithm_spec.EncryptionAlgorithmSpec"
    ]
    """<p>Specifies the encryption algorithm that KMS will use to encrypt the plaintext message. The algorithm must be compatible with the KMS key that you specify.</p> <p>This parameter is required only for asymmetric KMS keys. The default value, <code>SYMMETRIC_DEFAULT</code>, is the algorithm used for symmetric encryption KMS keys. If you are using an asymmetric KMS key, we recommend RSAES_OAEP_SHA_256.</p> <p>The SM2PKE algorithm is only available in China Regions.</p>"""
    dry_run: NotRequired["aws_sdk_kms.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter. </p> <p>To learn more about how to use this parameter, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html\">Testing your permissions</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
