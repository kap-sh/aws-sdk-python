"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#AccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.account_id

AccountIdList: TypeAlias = list["capo_cost_optimization_hub.types.account_id.AccountId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AccountIdList:
    return list(data)
