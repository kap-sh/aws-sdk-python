"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SecretsManagerEncryptionKeyConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.role_arn
    import aws_sdk_mediaconnect.types.secret_arn


class SecretsManagerEncryptionKeyConfiguration(TypedDict):
    secret_arn: "aws_sdk_mediaconnect.types.secret_arn.SecretArn"
    """<p>The ARN of the Secrets Manager secret used for transit encryption.</p>"""
    role_arn: "aws_sdk_mediaconnect.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role assumed by MediaConnect to access the Secrets Manager secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecretsManagerEncryptionKeyConfiguration) -> dict:
    out: dict = {}
    out["secretArn"] = value["secret_arn"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> SecretsManagerEncryptionKeyConfiguration:
    out: SecretsManagerEncryptionKeyConfiguration = {}  # type: ignore[typeddict-item]
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    else:
        raise DeserializationError(
            "SecretsManagerEncryptionKeyConfiguration.secret_arn required"
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError(
            "SecretsManagerEncryptionKeyConfiguration.role_arn required"
        )
    return out
