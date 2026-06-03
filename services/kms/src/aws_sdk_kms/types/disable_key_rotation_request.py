"""Generated from Smithy shape ``com.amazonaws.kms#DisableKeyRotationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kms.types.key_id_type


class DisableKeyRotationRequest(TypedDict):
    key_id: "aws_sdk_kms.types.key_id_type.KeyIdType"
    """<p>Identifies a symmetric encryption KMS key. You cannot enable or disable automatic rotation of <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html#asymmetric-cmks\">asymmetric KMS keys</a>, <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html\">HMAC KMS keys</a>, KMS keys with <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html\">imported key material</a>, or KMS keys in a <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html\">custom key store</a>.</p> <p>Specify the key ID or key ARN of the KMS key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
