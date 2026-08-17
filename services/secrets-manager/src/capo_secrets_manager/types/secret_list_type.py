"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_secrets_manager.types.secret_list_entry

SecretListType: TypeAlias = list[
    "capo_secrets_manager.types.secret_list_entry.SecretListEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecretListType) -> list:
    import capo_secrets_manager.types.secret_list_entry

    out: list = []
    for item in value:
        out.append(
            capo_secrets_manager.types.secret_list_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SecretListType:
    import capo_secrets_manager.types.secret_list_entry

    out: SecretListType = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_secrets_manager.types.secret_list_entry.deserialize_aws_json_1_1(item)
        )
    return out
