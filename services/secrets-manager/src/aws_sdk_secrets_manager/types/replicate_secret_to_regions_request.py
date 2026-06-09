"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ReplicateSecretToRegionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_secrets_manager.errors import DeserializationError

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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicateSecretToRegionsRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    import aws_sdk_secrets_manager.types.add_replica_region_list_type

    out["AddReplicaRegions"] = (
        aws_sdk_secrets_manager.types.add_replica_region_list_type.serialize_aws_json_1_1(
            value["add_replica_regions"]
        )
    )
    out["ForceOverwriteReplicaSecret"] = value.get(
        "force_overwrite_replica_secret", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicateSecretToRegionsRequest:
    out: ReplicateSecretToRegionsRequest = {}  # type: ignore[typeddict-item]
    if "SecretId" in data:
        out["secret_id"] = data["SecretId"]
    else:
        raise DeserializationError("ReplicateSecretToRegionsRequest.secret_id required")
    if "AddReplicaRegions" in data:
        import aws_sdk_secrets_manager.types.add_replica_region_list_type

        out["add_replica_regions"] = (
            aws_sdk_secrets_manager.types.add_replica_region_list_type.deserialize_aws_json_1_1(
                data["AddReplicaRegions"]
            )
        )
    else:
        raise DeserializationError(
            "ReplicateSecretToRegionsRequest.add_replica_regions required"
        )
    if "ForceOverwriteReplicaSecret" in data:
        out["force_overwrite_replica_secret"] = data["ForceOverwriteReplicaSecret"]
    else:
        out["force_overwrite_replica_secret"] = False
    return out
