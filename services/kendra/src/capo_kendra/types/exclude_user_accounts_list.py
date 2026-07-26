"""Generated from Smithy shape ``com.amazonaws.kendra#ExcludeUserAccountsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.user_account

ExcludeUserAccountsList: TypeAlias = list["capo_kendra.types.user_account.UserAccount"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExcludeUserAccountsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ExcludeUserAccountsList:
    return list(data)
