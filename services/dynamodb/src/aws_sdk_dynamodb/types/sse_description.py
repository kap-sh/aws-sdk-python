"""Generated from Smithy shape ``com.amazonaws.dynamodb#SSEDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.date
    import aws_sdk_dynamodb.types.kms_master_key_arn
    import aws_sdk_dynamodb.types.sse_status
    import aws_sdk_dynamodb.types.sse_type


class SSEDescription(TypedDict):
    status: NotRequired["aws_sdk_dynamodb.types.sse_status.SSEStatus"]
    """<p>Represents the current state of server-side encryption. The only supported values are:</p> <ul> <li> <p> <code>ENABLED</code> - Server-side encryption is enabled.</p> </li> <li> <p> <code>UPDATING</code> - Server-side encryption is being updated.</p> </li> </ul>"""
    sse_type: NotRequired["aws_sdk_dynamodb.types.sse_type.SSEType"]
    """<p>Server-side encryption type. The only supported value is:</p> <ul> <li> <p> <code>KMS</code> - Server-side encryption that uses Key Management Service. The key is stored in your account and is managed by KMS (KMS charges apply).</p> </li> </ul>"""
    kms_master_key_arn: NotRequired[
        "aws_sdk_dynamodb.types.kms_master_key_arn.KMSMasterKeyArn"
    ]
    """<p>The KMS key ARN used for the KMS encryption.</p>"""
    inaccessible_encryption_date_time: NotRequired["aws_sdk_dynamodb.types.date.Date"]
    """<p>Indicates the time, in UNIX epoch date format, when DynamoDB detected that the table's KMS key was inaccessible. This attribute will automatically be cleared when DynamoDB detects that the table's KMS key is accessible again. DynamoDB will initiate the table archival process when table's KMS key remains inaccessible for more than seven days from this date.</p>"""
