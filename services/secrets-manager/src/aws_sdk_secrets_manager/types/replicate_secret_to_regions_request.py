"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ReplicateSecretToRegionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.add_replica_region_list_type
    import aws_sdk_secrets_manager.types.boolean_type
    import aws_sdk_secrets_manager.types.secret_id_type


class ReplicateSecretToRegionsRequest(TypedDict):
    secret_id: "aws_sdk_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the secret to replicate.</p>"""
    add_replica_regions: "aws_sdk_secrets_manager.types.add_replica_region_list_type.AddReplicaRegionListType"
    """<p>A list of Regions in which to replicate the secret.</p>"""
    force_overwrite_replica_secret: (
        "aws_sdk_secrets_manager.types.boolean_type.BooleanType"
    )
    """<p>Specifies whether to overwrite a secret with the same name in the destination Region. By default, secrets aren't overwritten.</p>"""
