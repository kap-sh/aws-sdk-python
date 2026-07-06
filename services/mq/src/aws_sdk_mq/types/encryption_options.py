"""Generated from Smithy shape ``com.amazonaws.mq#EncryptionOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__boolean
    import aws_sdk_mq.types.__string


class EncryptionOptions(TypedDict, closed=True):
    kms_key_id: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The customer master key (CMK) to use for the A KMS (KMS). This key is used to encrypt your data at rest. If not provided, Amazon MQ will use a default CMK to encrypt your data.</p>"""
    use_aws_owned_key: NotRequired["aws_sdk_mq.types.__boolean.__boolean"]
    """<p>Enables the use of an Amazon Web Services owned CMK using KMS (KMS). Set to true by default, if no value is provided, for example, for RabbitMQ brokers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionOptions) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "use_aws_owned_key" in value:
        out["useAwsOwnedKey"] = value["use_aws_owned_key"]
    return out


def deserialize_json(data: dict) -> EncryptionOptions:
    out: EncryptionOptions = {}  # type: ignore[typeddict-item]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "useAwsOwnedKey" in data:
        out["use_aws_owned_key"] = data["useAwsOwnedKey"]
    return out
