"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AccountIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.account_id

AccountIds: TypeAlias = list["capo_cloudwatch_logs.types.account_id.AccountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AccountIds:
    return list(data)
