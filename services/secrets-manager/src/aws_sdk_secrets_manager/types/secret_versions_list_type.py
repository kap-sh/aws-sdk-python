"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretVersionsListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_versions_list_entry

SecretVersionsListType: TypeAlias = list[
    "aws_sdk_secrets_manager.types.secret_versions_list_entry.SecretVersionsListEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecretVersionsListType) -> list:
    import aws_sdk_secrets_manager.types.secret_versions_list_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_secrets_manager.types.secret_versions_list_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SecretVersionsListType:
    import aws_sdk_secrets_manager.types.secret_versions_list_entry

    out: SecretVersionsListType = []
    for item in data:
        out.append(
            aws_sdk_secrets_manager.types.secret_versions_list_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
