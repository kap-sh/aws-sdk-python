"""Generated from Smithy shape ``com.amazonaws.odb#OciEncryptionKeyConfiguration``."""

from typing import TypedDict

from aws_sdk_odb.errors import DeserializationError


class OciEncryptionKeyConfiguration(TypedDict):
    kms_key_id: "str"
    """<p>The Oracle Cloud Identifier (OCID) of the OCI Vault key to use for encryption.</p>"""
    vault_id: "str"
    """<p>The Oracle Cloud Identifier (OCID) of the OCI Vault that contains the encryption key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OciEncryptionKeyConfiguration) -> dict:
    out: dict = {}
    out["kmsKeyId"] = value["kms_key_id"]
    out["vaultId"] = value["vault_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> OciEncryptionKeyConfiguration:
    out: OciEncryptionKeyConfiguration = {}  # type: ignore[typeddict-item]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    else:
        raise DeserializationError("OciEncryptionKeyConfiguration.kms_key_id required")
    if "vaultId" in data:
        out["vault_id"] = data["vaultId"]
    else:
        raise DeserializationError("OciEncryptionKeyConfiguration.vault_id required")
    return out
