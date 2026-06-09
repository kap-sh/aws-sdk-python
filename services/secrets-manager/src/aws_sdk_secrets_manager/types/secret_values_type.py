"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretValuesType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_value_entry

SecretValuesType: TypeAlias = list[
    "aws_sdk_secrets_manager.types.secret_value_entry.SecretValueEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecretValuesType) -> list:
    import aws_sdk_secrets_manager.types.secret_value_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_secrets_manager.types.secret_value_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SecretValuesType:
    import aws_sdk_secrets_manager.types.secret_value_entry

    out: SecretValuesType = []
    for item in data:
        out.append(
            aws_sdk_secrets_manager.types.secret_value_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
