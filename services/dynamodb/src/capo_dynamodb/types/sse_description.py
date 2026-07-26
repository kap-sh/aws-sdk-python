"""Generated from Smithy shape ``com.amazonaws.dynamodb#SSEDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.date
    import capo_dynamodb.types.kms_master_key_arn
    import capo_dynamodb.types.sse_status
    import capo_dynamodb.types.sse_type


class SSEDescription(TypedDict, closed=True):
    status: NotRequired["capo_dynamodb.types.sse_status.SSEStatus"]
    """<p>Represents the current state of server-side encryption. The only supported values are:</p> <ul> <li> <p> <code>ENABLED</code> - Server-side encryption is enabled.</p> </li> <li> <p> <code>UPDATING</code> - Server-side encryption is being updated.</p> </li> </ul>"""
    sse_type: NotRequired["capo_dynamodb.types.sse_type.SSEType"]
    """<p>Server-side encryption type. The only supported value is:</p> <ul> <li> <p> <code>KMS</code> - Server-side encryption that uses Key Management Service. The key is stored in your account and is managed by KMS (KMS charges apply).</p> </li> </ul>"""
    kms_master_key_arn: NotRequired[
        "capo_dynamodb.types.kms_master_key_arn.KMSMasterKeyArn"
    ]
    """<p>The KMS key ARN used for the KMS encryption.</p>"""
    inaccessible_encryption_date_time: NotRequired["capo_dynamodb.types.date.Date"]
    """<p>Indicates the time, in UNIX epoch date format, when DynamoDB detected that the table's KMS key was inaccessible. This attribute will automatically be cleared when DynamoDB detects that the table's KMS key is accessible again. DynamoDB will initiate the table archival process when table's KMS key remains inaccessible for more than seven days from this date.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SSEDescription) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_dynamodb.types.sse_status

        out["Status"] = capo_dynamodb.types.sse_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "sse_type" in value:
        import capo_dynamodb.types.sse_type

        out["SSEType"] = capo_dynamodb.types.sse_type.serialize_aws_json_1_0(
            value["sse_type"]
        )
    if "kms_master_key_arn" in value:
        out["KMSMasterKeyArn"] = value["kms_master_key_arn"]
    if "inaccessible_encryption_date_time" in value:
        import capo_dynamodb.types.date

        out["InaccessibleEncryptionDateTime"] = (
            capo_dynamodb.types.date.serialize_aws_json_1_0(
                value["inaccessible_encryption_date_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SSEDescription:
    out: SSEDescription = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_dynamodb.types.sse_status

        out["status"] = capo_dynamodb.types.sse_status.deserialize_aws_json_1_0(
            data["Status"]
        )
    if "SSEType" in data:
        import capo_dynamodb.types.sse_type

        out["sse_type"] = capo_dynamodb.types.sse_type.deserialize_aws_json_1_0(
            data["SSEType"]
        )
    if "KMSMasterKeyArn" in data:
        out["kms_master_key_arn"] = data["KMSMasterKeyArn"]
    if "InaccessibleEncryptionDateTime" in data:
        import capo_dynamodb.types.date

        out["inaccessible_encryption_date_time"] = (
            capo_dynamodb.types.date.deserialize_aws_json_1_0(
                data["InaccessibleEncryptionDateTime"]
            )
        )
    return out
