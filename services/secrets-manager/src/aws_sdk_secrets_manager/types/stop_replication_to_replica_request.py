"""Generated from Smithy shape ``com.amazonaws.secretsmanager#StopReplicationToReplicaRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_id_type


class StopReplicationToReplicaRequest(TypedDict):
    secret_id: "aws_sdk_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The name of the secret or the replica ARN. The replica ARN is the same as the original primary secret ARN expect the Region is changed to the replica Region. </p>"""
