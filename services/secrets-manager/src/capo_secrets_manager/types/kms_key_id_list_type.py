"""Generated from Smithy shape ``com.amazonaws.secretsmanager#KmsKeyIdListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_secrets_manager.types.kms_key_id_type

KmsKeyIdListType: TypeAlias = list[
    "capo_secrets_manager.types.kms_key_id_type.KmsKeyIdType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KmsKeyIdListType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> KmsKeyIdListType:
    return list(data)
