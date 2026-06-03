"""Generated from Smithy shape ``com.amazonaws.kms#RevokeGrantRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.grant_id_type
    import aws_sdk_kms.types.key_id_type
    import aws_sdk_kms.types.nullable_boolean_type


class RevokeGrantRequest(TypedDict):
    key_id: "aws_sdk_kms.types.key_id_type.KeyIdType"
    """<p>A unique identifier for the KMS key associated with the grant. To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p> <p>Specify the key ID or key ARN of the KMS key. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    grant_id: "aws_sdk_kms.types.grant_id_type.GrantIdType"
    """<p>Identifies the grant to revoke. To get the grant ID, use <a>CreateGrant</a>, <a>ListGrants</a>, or <a>ListRetirableGrants</a>.</p>"""
    dry_run: NotRequired["aws_sdk_kms.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter. </p> <p>To learn more about how to use this parameter, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html\">Testing your permissions</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
