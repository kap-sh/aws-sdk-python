"""Generated from Smithy shape ``com.amazonaws.configservice#AccountAggregationSourceAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.account_id

AccountAggregationSourceAccountList: TypeAlias = list[
    "capo_config_service.types.account_id.AccountId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountAggregationSourceAccountList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AccountAggregationSourceAccountList:
    return list(data)
