"""Generated from Smithy shape ``com.amazonaws.kms#GetKeyPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.key_id_type
    import aws_sdk_kms.types.policy_name_type


class GetKeyPolicyRequest(TypedDict):
    key_id: "aws_sdk_kms.types.key_id_type.KeyIdType"
    """<p>Gets the key policy for the specified KMS key.</p> <p>Specify the key ID or key ARN of the KMS key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    policy_name: NotRequired["aws_sdk_kms.types.policy_name_type.PolicyNameType"]
    """<p>Specifies the name of the key policy. If no policy name is specified, the default value is <code>default</code>. The only valid name is <code>default</code>. To get the names of key policies, use <a>ListKeyPolicies</a>.</p>"""
