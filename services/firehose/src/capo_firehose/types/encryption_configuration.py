"""Generated from Smithy shape ``com.amazonaws.firehose#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.kms_encryption_config
    import capo_firehose.types.no_encryption_config


class EncryptionConfiguration(TypedDict, closed=True):
    no_encryption_config: NotRequired[
        "capo_firehose.types.no_encryption_config.NoEncryptionConfig"
    ]
    """<p>Specifically override existing encryption information to ensure that no encryption is used.</p>"""
    kms_encryption_config: NotRequired[
        "capo_firehose.types.kms_encryption_config.KMSEncryptionConfig"
    ]
    """<p>The encryption key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    if "no_encryption_config" in value:
        import capo_firehose.types.no_encryption_config

        out["NoEncryptionConfig"] = (
            capo_firehose.types.no_encryption_config.serialize_aws_json_1_1(
                value["no_encryption_config"]
            )
        )
    if "kms_encryption_config" in value:
        import capo_firehose.types.kms_encryption_config

        out["KMSEncryptionConfig"] = (
            capo_firehose.types.kms_encryption_config.serialize_aws_json_1_1(
                value["kms_encryption_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "NoEncryptionConfig" in data:
        import capo_firehose.types.no_encryption_config

        out["no_encryption_config"] = (
            capo_firehose.types.no_encryption_config.deserialize_aws_json_1_1(
                data["NoEncryptionConfig"]
            )
        )
    if "KMSEncryptionConfig" in data:
        import capo_firehose.types.kms_encryption_config

        out["kms_encryption_config"] = (
            capo_firehose.types.kms_encryption_config.deserialize_aws_json_1_1(
                data["KMSEncryptionConfig"]
            )
        )
    return out
