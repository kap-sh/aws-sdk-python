"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#SecretsManager``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.secrets_manager_arn
    import aws_sdk_iot_managed_integrations.types.secrets_manager_version_id


class SecretsManager(TypedDict, closed=True):
    arn: "aws_sdk_iot_managed_integrations.types.secrets_manager_arn.SecretsManagerArn"
    """<p>The Amazon Resource Name (ARN) of the AWS Secrets Manager secret.</p>"""
    version_id: "aws_sdk_iot_managed_integrations.types.secrets_manager_version_id.SecretsManagerVersionId"
    """<p>The version ID of the AWS Secrets Manager secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecretsManager) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["versionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> SecretsManager:
    out: SecretsManager = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("SecretsManager.arn required")
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    else:
        raise DeserializationError("SecretsManager.version_id required")
    return out
