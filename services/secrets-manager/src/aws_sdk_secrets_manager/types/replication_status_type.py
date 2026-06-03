"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ReplicationStatusType``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.kms_key_id_type
    import aws_sdk_secrets_manager.types.last_accessed_date_type
    import aws_sdk_secrets_manager.types.region_type
    import aws_sdk_secrets_manager.types.status_message_type
    import aws_sdk_secrets_manager.types.status_type


class ReplicationStatusType(TypedDict):
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
    """<p>Status message such as \"<i>Secret with this name already exists in this region</i>\".</p>"""
    last_accessed_date: NotRequired[
        "aws_sdk_secrets_manager.types.last_accessed_date_type.LastAccessedDateType"
    ]
    """<p>The date that the secret was last accessed in the Region. This field is omitted if the secret has never been retrieved in the Region.</p>"""
