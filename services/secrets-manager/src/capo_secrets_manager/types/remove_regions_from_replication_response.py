"""Generated from Smithy shape ``com.amazonaws.secretsmanager#RemoveRegionsFromReplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.replication_status_list_type
    import capo_secrets_manager.types.secret_arn_type


class RemoveRegionsFromReplicationResponse(TypedDict, closed=True):
    arn: NotRequired["capo_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the primary secret.</p>"""
    replication_status: NotRequired[
        "capo_secrets_manager.types.replication_status_list_type.ReplicationStatusListType"
    ]
    """<p>The status of replicas for this secret after you remove Regions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveRegionsFromReplicationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "replication_status" in value:
        import capo_secrets_manager.types.replication_status_list_type

        out["ReplicationStatus"] = (
            capo_secrets_manager.types.replication_status_list_type.serialize_aws_json_1_1(
                value["replication_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveRegionsFromReplicationResponse:
    out: RemoveRegionsFromReplicationResponse = {}  # type: ignore[typeddict-item]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    if "ReplicationStatus" in data:
        import capo_secrets_manager.types.replication_status_list_type

        out["replication_status"] = (
            capo_secrets_manager.types.replication_status_list_type.deserialize_aws_json_1_1(
                data["ReplicationStatus"]
            )
        )
    return out
