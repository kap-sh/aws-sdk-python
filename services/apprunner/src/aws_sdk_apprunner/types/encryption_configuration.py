"""Generated from Smithy shape ``com.amazonaws.apprunner#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.kms_key_arn


class EncryptionConfiguration(TypedDict, closed=True):
    kms_key: "aws_sdk_apprunner.types.kms_key_arn.KmsKeyArn"
    """<p>The ARN of the KMS key that's used for encryption.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    out["KmsKey"] = value["kms_key"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "KmsKey" in data:
        out["kms_key"] = data["KmsKey"]
    else:
        raise DeserializationError("EncryptionConfiguration.kms_key required")
    return out
