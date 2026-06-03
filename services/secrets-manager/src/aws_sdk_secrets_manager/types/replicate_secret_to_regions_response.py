"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ReplicateSecretToRegionsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.replication_status_list_type
    import aws_sdk_secrets_manager.types.secret_arn_type


class ReplicateSecretToRegionsResponse(TypedDict):
    arn: NotRequired["aws_sdk_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the primary secret.</p>"""
    replication_status: NotRequired[
        "aws_sdk_secrets_manager.types.replication_status_list_type.ReplicationStatusListType"
    ]
    """<p>The status of replication.</p>"""
