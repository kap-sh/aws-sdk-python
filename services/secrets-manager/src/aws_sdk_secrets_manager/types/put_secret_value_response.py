"""Generated from Smithy shape ``com.amazonaws.secretsmanager#PutSecretValueResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_arn_type
    import aws_sdk_secrets_manager.types.secret_name_type
    import aws_sdk_secrets_manager.types.secret_version_id_type
    import aws_sdk_secrets_manager.types.secret_version_stages_type


class PutSecretValueResponse(TypedDict):
    arn: NotRequired["aws_sdk_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the secret.</p>"""
    name: NotRequired["aws_sdk_secrets_manager.types.secret_name_type.SecretNameType"]
    """<p>The name of the secret.</p>"""
    version_id: NotRequired[
        "aws_sdk_secrets_manager.types.secret_version_id_type.SecretVersionIdType"
    ]
    """<p>The unique identifier of the version of the secret.</p>"""
    version_stages: NotRequired[
        "aws_sdk_secrets_manager.types.secret_version_stages_type.SecretVersionStagesType"
    ]
    """<p>The list of staging labels that are currently attached to this version of the secret. Secrets Manager uses staging labels to track a version as it progresses through the secret rotation process.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutSecretValueResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "version_stages" in value:
        import aws_sdk_secrets_manager.types.secret_version_stages_type

        out["VersionStages"] = (
            aws_sdk_secrets_manager.types.secret_version_stages_type.serialize_aws_json_1_1(
                value["version_stages"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutSecretValueResponse:
    out: PutSecretValueResponse = {}  # type: ignore[typeddict-item]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    if "VersionStages" in data:
        import aws_sdk_secrets_manager.types.secret_version_stages_type

        out["version_stages"] = (
            aws_sdk_secrets_manager.types.secret_version_stages_type.deserialize_aws_json_1_1(
                data["VersionStages"]
            )
        )
    return out
