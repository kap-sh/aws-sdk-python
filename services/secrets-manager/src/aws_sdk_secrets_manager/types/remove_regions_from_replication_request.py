"""Generated from Smithy shape ``com.amazonaws.secretsmanager#RemoveRegionsFromReplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.remove_replica_region_list_type
    import aws_sdk_secrets_manager.types.secret_id_type


class RemoveRegionsFromReplicationRequest(TypedDict):
    secret_id: "aws_sdk_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the secret.</p>"""
    remove_replica_regions: "aws_sdk_secrets_manager.types.remove_replica_region_list_type.RemoveReplicaRegionListType"
    """<p>The Regions of the replicas to remove.</p>"""
