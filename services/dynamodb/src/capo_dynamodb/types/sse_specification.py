"""Generated from Smithy shape ``com.amazonaws.dynamodb#SSESpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.kms_master_key_id
    import capo_dynamodb.types.sse_enabled
    import capo_dynamodb.types.sse_type


class SSESpecification(TypedDict, closed=True):
    enabled: NotRequired["capo_dynamodb.types.sse_enabled.SSEEnabled"]
    """<p>Indicates whether server-side encryption is done using an Amazon Web Services managed key or an Amazon Web Services owned key. If enabled (true), server-side encryption type is set to <code>KMS</code> and an Amazon Web Services managed key is used (KMS charges apply). If disabled (false) or not specified, server-side encryption is set to Amazon Web Services owned key.</p>"""
    sse_type: NotRequired["capo_dynamodb.types.sse_type.SSEType"]
    """<p>Server-side encryption type. The only supported value is:</p> <ul> <li> <p> <code>KMS</code> - Server-side encryption that uses Key Management Service. The key is stored in your account and is managed by KMS (KMS charges apply).</p> </li> </ul>"""
    kms_master_key_id: NotRequired[
        "capo_dynamodb.types.kms_master_key_id.KMSMasterKeyId"
    ]
    """<p>The KMS key that should be used for the KMS encryption. To specify a key, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB key <code>alias/aws/dynamodb</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SSESpecification) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "sse_type" in value:
        import capo_dynamodb.types.sse_type

        out["SSEType"] = capo_dynamodb.types.sse_type.serialize_aws_json_1_0(
            value["sse_type"]
        )
    if "kms_master_key_id" in value:
        out["KMSMasterKeyId"] = value["kms_master_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SSESpecification:
    out: SSESpecification = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("SSEType") is not None:
        import capo_dynamodb.types.sse_type

        out["sse_type"] = capo_dynamodb.types.sse_type.deserialize_aws_json_1_0(
            data["SSEType"]
        )
    if data.get("KMSMasterKeyId") is not None:
        out["kms_master_key_id"] = data["KMSMasterKeyId"]
    return out
