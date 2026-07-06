"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ReplicationStatusType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.kms_key_id_type
    import aws_sdk_secrets_manager.types.last_accessed_date_type
    import aws_sdk_secrets_manager.types.region_type
    import aws_sdk_secrets_manager.types.status_message_type
    import aws_sdk_secrets_manager.types.status_type


class ReplicationStatusType(TypedDict, closed=True):
    region: NotRequired["aws_sdk_secrets_manager.types.region_type.RegionType"]
    """<p>The Region where replication occurs.</p>"""
    kms_key_id: NotRequired[
        "aws_sdk_secrets_manager.types.kms_key_id_type.KmsKeyIdType"
    ]
    """<p>Can be an <code>ARN</code>, <code>Key ID</code>, or <code>Alias</code>. </p>"""
    status: NotRequired["aws_sdk_secrets_manager.types.status_type.StatusType"]
    """<p>The status can be <code>InProgress</code>, <code>Failed</code>, or <code>InSync</code>.</p>"""
    status_message: NotRequired[
        "aws_sdk_secrets_manager.types.status_message_type.StatusMessageType"
    ]
    r"""<p>Status message such as \"<i>Secret with this name already exists in this region</i>\".</p>"""
    last_accessed_date: NotRequired[
        "aws_sdk_secrets_manager.types.last_accessed_date_type.LastAccessedDateType"
    ]
    """<p>The date that the secret was last accessed in the Region. This field is omitted if the secret has never been retrieved in the Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationStatusType) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "status" in value:
        import aws_sdk_secrets_manager.types.status_type

        out["Status"] = (
            aws_sdk_secrets_manager.types.status_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "last_accessed_date" in value:
        import aws_sdk_secrets_manager.types.last_accessed_date_type

        out["LastAccessedDate"] = (
            aws_sdk_secrets_manager.types.last_accessed_date_type.serialize_aws_json_1_1(
                value["last_accessed_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationStatusType:
    out: ReplicationStatusType = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "Status" in data:
        import aws_sdk_secrets_manager.types.status_type

        out["status"] = (
            aws_sdk_secrets_manager.types.status_type.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "LastAccessedDate" in data:
        import aws_sdk_secrets_manager.types.last_accessed_date_type

        out["last_accessed_date"] = (
            aws_sdk_secrets_manager.types.last_accessed_date_type.deserialize_aws_json_1_1(
                data["LastAccessedDate"]
            )
        )
    return out
