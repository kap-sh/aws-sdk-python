"""Generated from Smithy shape ``com.amazonaws.dynamodb#SSESpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.kms_master_key_id
    import aws_sdk_dynamodb.types.sse_enabled
    import aws_sdk_dynamodb.types.sse_type


class SSESpecification(TypedDict):
    enabled: NotRequired["aws_sdk_dynamodb.types.sse_enabled.SSEEnabled"]
    """<p>Indicates whether server-side encryption is done using an Amazon Web Services managed key or an Amazon Web Services owned key. If enabled (true), server-side encryption type is set to <code>KMS</code> and an Amazon Web Services managed key is used (KMS charges apply). If disabled (false) or not specified, server-side encryption is set to Amazon Web Services owned key.</p>"""
    sse_type: NotRequired["aws_sdk_dynamodb.types.sse_type.SSEType"]
    """<p>Server-side encryption type. The only supported value is:</p> <ul> <li> <p> <code>KMS</code> - Server-side encryption that uses Key Management Service. The key is stored in your account and is managed by KMS (KMS charges apply).</p> </li> </ul>"""
    kms_master_key_id: NotRequired[
        "aws_sdk_dynamodb.types.kms_master_key_id.KMSMasterKeyId"
    ]
    """<p>The KMS key that should be used for the KMS encryption. To specify a key, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB key <code>alias/aws/dynamodb</code>.</p>"""
