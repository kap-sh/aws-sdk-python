"""Generated from Smithy shape ``com.amazonaws.kms#GenerateMacRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.grant_token_list
    import awd_sdk_kms.types.key_id_type
    import awd_sdk_kms.types.mac_algorithm_spec
    import awd_sdk_kms.types.nullable_boolean_type
    import awd_sdk_kms.types.plaintext_type


class GenerateMacRequest(TypedDict):
    message: "awd_sdk_kms.types.plaintext_type.PlaintextType"
    """<p>The message to be hashed. Specify a message of up to 4,096 bytes. </p> <p> <code>GenerateMac</code> and <a>VerifyMac</a> do not provide special handling for message digests. If you generate an HMAC for a hash digest of a message, you must verify the HMAC of the same hash digest.</p>"""
    key_id: "awd_sdk_kms.types.key_id_type.KeyIdType"
    """<p>The HMAC KMS key to use in the operation. The MAC algorithm computes the HMAC for the message and the key as described in <a href=\"https://datatracker.ietf.org/doc/html/rfc2104\">RFC 2104</a>.</p> <p>To identify an HMAC KMS key, use the <a>DescribeKey</a> operation and see the <code>KeySpec</code> field in the response.</p>"""
    mac_algorithm: "awd_sdk_kms.types.mac_algorithm_spec.MacAlgorithmSpec"
    """<p>The MAC algorithm used in the operation.</p> <p> The algorithm must be compatible with the HMAC KMS key that you specify. To find the MAC algorithms that your HMAC KMS key supports, use the <a>DescribeKey</a> operation and see the <code>MacAlgorithms</code> field in the <code>DescribeKey</code> response.</p>"""
    grant_tokens: NotRequired["awd_sdk_kms.types.grant_token_list.GrantTokenList"]
    """<p>A list of grant tokens.</p> <p>Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved <i>eventual consistency</i>. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token\">Grant token</a> and <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html\">Using a grant token</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    dry_run: NotRequired["awd_sdk_kms.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter. </p> <p>To learn more about how to use this parameter, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html\">Testing your permissions</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
