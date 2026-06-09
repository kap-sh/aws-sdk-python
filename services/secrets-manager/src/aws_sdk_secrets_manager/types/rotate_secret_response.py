"""Generated from Smithy shape ``com.amazonaws.secretsmanager#RotateSecretResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_arn_type
    import aws_sdk_secrets_manager.types.secret_name_type
    import aws_sdk_secrets_manager.types.secret_version_id_type


class RotateSecretResponse(TypedDict):
    arn: NotRequired["aws_sdk_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the secret.</p>"""
    name: NotRequired["aws_sdk_secrets_manager.types.secret_name_type.SecretNameType"]
    """<p>The name of the secret.</p>"""
    version_id: NotRequired[
        "aws_sdk_secrets_manager.types.secret_version_id_type.SecretVersionIdType"
    ]
    """<p>The ID of the new version of the secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotateSecretResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RotateSecretResponse:
    out: RotateSecretResponse = {}  # type: ignore[typeddict-item]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    return out
