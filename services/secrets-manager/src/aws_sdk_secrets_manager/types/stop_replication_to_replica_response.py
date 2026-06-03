"""Generated from Smithy shape ``com.amazonaws.secretsmanager#StopReplicationToReplicaResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_arn_type


class StopReplicationToReplicaResponse(TypedDict):
    arn: NotRequired["aws_sdk_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the promoted secret. The ARN is the same as the original primary secret except the Region is changed.</p>"""
