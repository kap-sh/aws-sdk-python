"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretIdListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_secrets_manager.types.secret_id_type

SecretIdListType: TypeAlias = list[
    "capo_secrets_manager.types.secret_id_type.SecretIdType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecretIdListType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SecretIdListType:
    return list(data)
