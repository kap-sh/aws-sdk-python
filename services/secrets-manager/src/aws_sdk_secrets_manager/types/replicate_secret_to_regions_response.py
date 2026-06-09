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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicateSecretToRegionsResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "replication_status" in value:
        import aws_sdk_secrets_manager.types.replication_status_list_type

        out["ReplicationStatus"] = (
            aws_sdk_secrets_manager.types.replication_status_list_type.serialize_aws_json_1_1(
                value["replication_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicateSecretToRegionsResponse:
    out: ReplicateSecretToRegionsResponse = {}  # type: ignore[typeddict-item]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    if "ReplicationStatus" in data:
        import aws_sdk_secrets_manager.types.replication_status_list_type

        out["replication_status"] = (
            aws_sdk_secrets_manager.types.replication_status_list_type.deserialize_aws_json_1_1(
                data["ReplicationStatus"]
            )
        )
    return out
