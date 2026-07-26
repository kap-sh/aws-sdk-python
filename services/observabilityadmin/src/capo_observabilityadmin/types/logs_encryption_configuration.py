"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#LogsEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.encryption_conflict_resolution_strategy
    import capo_observabilityadmin.types.encryption_strategy
    import capo_observabilityadmin.types.resource_arn


class LogsEncryptionConfiguration(TypedDict, closed=True):
    encryption_strategy: (
        "capo_observabilityadmin.types.encryption_strategy.EncryptionStrategy"
    )
    """<p>Configuration that determines the encryption strategy of the destination log groups. CUSTOMER_MANAGED uses the configured KmsKeyArn to encrypt newly created destination log groups.</p>"""
    kms_key_arn: NotRequired["capo_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p>KMS Key ARN belonging to the primary destination account and region, to encrypt newly created central log groups in the primary destination.</p>"""
    encryption_conflict_resolution_strategy: NotRequired[
        "capo_observabilityadmin.types.encryption_conflict_resolution_strategy.EncryptionConflictResolutionStrategy"
    ]
    """<p>Conflict resolution strategy for centralization if the encryption strategy is set to CUSTOMER_MANAGED and the destination log group is encrypted with an AWS_OWNED KMS Key. ALLOW lets centralization go through while SKIP prevents centralization into the destination log group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogsEncryptionConfiguration) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.encryption_strategy

    out["EncryptionStrategy"] = (
        capo_observabilityadmin.types.encryption_strategy.serialize_json(
            value["encryption_strategy"]
        )
    )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "encryption_conflict_resolution_strategy" in value:
        import capo_observabilityadmin.types.encryption_conflict_resolution_strategy

        out["EncryptionConflictResolutionStrategy"] = (
            capo_observabilityadmin.types.encryption_conflict_resolution_strategy.serialize_json(
                value["encryption_conflict_resolution_strategy"]
            )
        )
    return out


def deserialize_json(data: dict) -> LogsEncryptionConfiguration:
    out: LogsEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "EncryptionStrategy" in data:
        import capo_observabilityadmin.types.encryption_strategy

        out["encryption_strategy"] = (
            capo_observabilityadmin.types.encryption_strategy.deserialize_json(
                data["EncryptionStrategy"]
            )
        )
    else:
        raise DeserializationError(
            "LogsEncryptionConfiguration.encryption_strategy required"
        )
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if "EncryptionConflictResolutionStrategy" in data:
        import capo_observabilityadmin.types.encryption_conflict_resolution_strategy

        out["encryption_conflict_resolution_strategy"] = (
            capo_observabilityadmin.types.encryption_conflict_resolution_strategy.deserialize_json(
                data["EncryptionConflictResolutionStrategy"]
            )
        )
    return out
