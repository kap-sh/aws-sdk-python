"""Generated from Smithy shape ``com.amazonaws.kms#UpdateKeyDescriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import awd_sdk_kms.types.description_type
    import awd_sdk_kms.types.key_id_type


class UpdateKeyDescriptionRequest(TypedDict):
    key_id: "awd_sdk_kms.types.key_id_type.KeyIdType"
    """<p>Updates the description of the specified KMS key.</p> <p>Specify the key ID or key ARN of the KMS key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    description: "awd_sdk_kms.types.description_type.DescriptionType"
    """<p>New description for the KMS key.</p> <important> <p>Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important>"""
