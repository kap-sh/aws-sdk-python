"""Generated from Smithy shape ``com.amazonaws.emrserverless#ManagedPersistenceMonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.encryption_key_arn


class ManagedPersistenceMonitoringConfiguration(TypedDict, closed=True):
    enabled: NotRequired["bool"]
    """<p>Enables managed logging and defaults to true. If set to false, managed logging will be turned off.</p>"""
    encryption_key_arn: NotRequired[
        "capo_emr_serverless.types.encryption_key_arn.EncryptionKeyArn"
    ]
    """<p>The KMS key ARN to encrypt the logs stored in managed log persistence.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedPersistenceMonitoringConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> ManagedPersistenceMonitoringConfiguration:
    out: ManagedPersistenceMonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    return out
