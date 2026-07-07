"""Generated from Smithy shape ``com.amazonaws.healthlake#SseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.kms_encryption_config


class SseConfiguration(TypedDict, closed=True):
    kms_encryption_config: (
        "aws_sdk_healthlake.types.kms_encryption_config.KmsEncryptionConfig"
    )
    """<p>The Key Management Service (KMS) encryption configuration used to provide details for data encryption.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SseConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_healthlake.types.kms_encryption_config

    out["KmsEncryptionConfig"] = (
        aws_sdk_healthlake.types.kms_encryption_config.serialize_aws_json_1_0(
            value["kms_encryption_config"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> SseConfiguration:
    out: SseConfiguration = {}  # type: ignore[typeddict-item]
    if "KmsEncryptionConfig" in data:
        import aws_sdk_healthlake.types.kms_encryption_config

        out["kms_encryption_config"] = (
            aws_sdk_healthlake.types.kms_encryption_config.deserialize_aws_json_1_0(
                data["KmsEncryptionConfig"]
            )
        )
    else:
        raise DeserializationError("SseConfiguration.kms_encryption_config required")
    return out
