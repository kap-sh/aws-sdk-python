"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAmazonMqBrokerEncryptionOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsAmazonMqBrokerEncryptionOptionsDetails(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The KMS key that’s used to encrypt your data at rest. If not provided, Amazon MQ will use a default KMS key to encrypt your data. </p>"""
    use_aws_owned_key: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Specifies that an KMS key should be used for at-rest encryption. Set to <code>true</code> by default if no value is provided (for example, for RabbitMQ brokers). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAmazonMqBrokerEncryptionOptionsDetails) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "use_aws_owned_key" in value:
        out["UseAwsOwnedKey"] = value["use_aws_owned_key"]
    return out


def deserialize_json(data: dict) -> AwsAmazonMqBrokerEncryptionOptionsDetails:
    out: AwsAmazonMqBrokerEncryptionOptionsDetails = {}  # type: ignore[typeddict-item]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "UseAwsOwnedKey" in data:
        out["use_aws_owned_key"] = data["UseAwsOwnedKey"]
    return out
