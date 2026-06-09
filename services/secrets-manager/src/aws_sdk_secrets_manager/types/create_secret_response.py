"""Generated from Smithy shape ``com.amazonaws.secretsmanager#CreateSecretResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.replication_status_list_type
    import aws_sdk_secrets_manager.types.secret_arn_type
    import aws_sdk_secrets_manager.types.secret_name_type
    import aws_sdk_secrets_manager.types.secret_version_id_type


class CreateSecretResponse(TypedDict):
    arn: NotRequired["aws_sdk_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the new secret. The ARN includes the name of the secret followed by six random characters. This ensures that if you create a new secret with the same name as a deleted secret, then users with access to the old secret don't get access to the new secret because the ARNs are different.</p>"""
    name: NotRequired["aws_sdk_secrets_manager.types.secret_name_type.SecretNameType"]
    """<p>The name of the new secret.</p>"""
    version_id: NotRequired[
        "aws_sdk_secrets_manager.types.secret_version_id_type.SecretVersionIdType"
    ]
    """<p>The unique identifier associated with the version of the new secret.</p>"""
    replication_status: NotRequired[
        "aws_sdk_secrets_manager.types.replication_status_list_type.ReplicationStatusListType"
    ]
    """<p>A list of the replicas of this secret and their status:</p> <ul> <li> <p> <code>Failed</code>, which indicates that the replica was not created.</p> </li> <li> <p> <code>InProgress</code>, which indicates that Secrets Manager is in the process of creating the replica.</p> </li> <li> <p> <code>InSync</code>, which indicates that the replica was created.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSecretResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "replication_status" in value:
        import aws_sdk_secrets_manager.types.replication_status_list_type

        out["ReplicationStatus"] = (
            aws_sdk_secrets_manager.types.replication_status_list_type.serialize_aws_json_1_1(
                value["replication_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSecretResponse:
    out: CreateSecretResponse = {}  # type: ignore[typeddict-item]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    if "ReplicationStatus" in data:
        import aws_sdk_secrets_manager.types.replication_status_list_type

        out["replication_status"] = (
            aws_sdk_secrets_manager.types.replication_status_list_type.deserialize_aws_json_1_1(
                data["ReplicationStatus"]
            )
        )
    return out
