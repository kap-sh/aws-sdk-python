"""Generated from Smithy shape ``com.amazonaws.kafka#EncryptionAtRest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class EncryptionAtRest(TypedDict, closed=True):
    data_volume_kms_key_id: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The ARN of the AWS KMS key for encrypting data at rest. If you don't specify a KMS key, MSK creates one for you and uses it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionAtRest) -> dict:
    out: dict = {}
    if "data_volume_kms_key_id" in value:
        out["dataVolumeKMSKeyId"] = value["data_volume_kms_key_id"]
    return out


def deserialize_json(data: dict) -> EncryptionAtRest:
    out: EncryptionAtRest = {}  # type: ignore[typeddict-item]
    if "dataVolumeKMSKeyId" in data:
        out["data_volume_kms_key_id"] = data["dataVolumeKMSKeyId"]
    return out
