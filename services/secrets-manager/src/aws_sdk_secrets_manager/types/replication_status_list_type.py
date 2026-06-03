"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ReplicationStatusListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.replication_status_type

ReplicationStatusListType: TypeAlias = list[
    "aws_sdk_secrets_manager.types.replication_status_type.ReplicationStatusType"
]
