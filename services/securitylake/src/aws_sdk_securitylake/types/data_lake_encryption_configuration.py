"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeEncryptionConfiguration``."""

from typing import TypedDict
from typing_extensions import NotRequired

class DataLakeEncryptionConfiguration(TypedDict):
    kms_key_id: NotRequired["str"]
    """<p>The identifier of KMS encryption key used by Amazon Security Lake to encrypt the Security Lake object.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DataLakeEncryptionConfiguration) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> DataLakeEncryptionConfiguration:
    out: DataLakeEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    return out