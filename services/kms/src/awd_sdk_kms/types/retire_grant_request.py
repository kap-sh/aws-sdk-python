"""Generated from Smithy shape ``com.amazonaws.kms#RetireGrantRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.grant_id_type
    import awd_sdk_kms.types.grant_token_type
    import awd_sdk_kms.types.key_id_type
    import awd_sdk_kms.types.nullable_boolean_type


class RetireGrantRequest(TypedDict):
    grant_token: NotRequired["awd_sdk_kms.types.grant_token_type.GrantTokenType"]
    """<p>Identifies the grant to be retired. You can use a grant token to identify a new grant even before it has achieved eventual consistency.</p> <p>Only the <a>CreateGrant</a> operation returns a grant token. For details, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token\">Grant token</a> and <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#terms-eventual-consistency\">Eventual consistency</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    key_id: NotRequired["awd_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The key ARN KMS key associated with the grant. To find the key ARN, use the <a>ListKeys</a> operation.</p> <p>For example: <code>arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p>"""
    grant_id: NotRequired["awd_sdk_kms.types.grant_id_type.GrantIdType"]
    """<p>Identifies the grant to retire. To get the grant ID, use <a>CreateGrant</a>, <a>ListGrants</a>, or <a>ListRetirableGrants</a>.</p> <ul> <li> <p>Grant ID Example - 0123456789012345678901234567890123456789012345678901234567890123</p> </li> </ul>"""
    dry_run: NotRequired["awd_sdk_kms.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter. </p> <p>To learn more about how to use this parameter, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html\">Testing your permissions</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
