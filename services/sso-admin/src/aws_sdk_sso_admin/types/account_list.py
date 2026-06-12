"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.account_id

AccountList: TypeAlias = list["aws_sdk_sso_admin.types.account_id.AccountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AccountList:
    return list(data)
