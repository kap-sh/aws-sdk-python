"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ServerSideEncryptionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.arn


class ServerSideEncryptionConfiguration(TypedDict):
    kms_key_arn: "aws_sdk_chime_sdk_voice.types.arn.Arn"
    """<p>The ARN of the KMS key used to encrypt the enrollment data in a voice profile domain. Asymmetric customer managed keys are not supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerSideEncryptionConfiguration) -> dict:
    out: dict = {}
    out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> ServerSideEncryptionConfiguration:
    out: ServerSideEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    else:
        raise DeserializationError(
            "ServerSideEncryptionConfiguration.kms_key_arn required"
        )
    return out
