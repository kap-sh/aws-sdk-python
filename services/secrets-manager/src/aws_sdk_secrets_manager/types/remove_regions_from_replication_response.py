"""Generated from Smithy shape ``com.amazonaws.secretsmanager#RemoveRegionsFromReplicationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.replication_status_list_type
    import aws_sdk_secrets_manager.types.secret_arn_type


class RemoveRegionsFromReplicationResponse(TypedDict):
    arn: NotRequired["aws_sdk_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the primary secret.</p>"""
    replication_status: NotRequired[
        "aws_sdk_secrets_manager.types.replication_status_list_type.ReplicationStatusListType"
    ]
    """<p>The status of replicas for this secret after you remove Regions.</p>"""
