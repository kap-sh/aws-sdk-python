"""Generated from Smithy shape ``com.amazonaws.ssm#Accounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.account

Accounts: TypeAlias = list["capo_ssm.types.account.Account"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Accounts) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Accounts:
    return list(data)
