"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.account_id

AccountIdList: TypeAlias = list["aws_sdk_compute_optimizer_automation.types.account_id.AccountId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AccountIdList:
    return list(data)