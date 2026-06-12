"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#SecretsManagerSecretConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.secrets_manager_secret_kms_id
    import aws_sdk_accessanalyzer.types.secrets_manager_secret_policy


class SecretsManagerSecretConfiguration(TypedDict):
    kms_key_id: NotRequired[
        "aws_sdk_accessanalyzer.types.secrets_manager_secret_kms_id.SecretsManagerSecretKmsId"
    ]
    """<p>The proposed ARN, key ID, or alias of the KMS key.</p>"""
    secret_policy: NotRequired[
        "aws_sdk_accessanalyzer.types.secrets_manager_secret_policy.SecretsManagerSecretPolicy"
    ]
    """<p>The proposed resource policy defining who can access or manage the secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecretsManagerSecretConfiguration) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "secret_policy" in value:
        out["secretPolicy"] = value["secret_policy"]
    return out


def deserialize_json(data: dict) -> SecretsManagerSecretConfiguration:
    out: SecretsManagerSecretConfiguration = {}  # type: ignore[typeddict-item]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "secretPolicy" in data:
        out["secret_policy"] = data["secretPolicy"]
    return out
