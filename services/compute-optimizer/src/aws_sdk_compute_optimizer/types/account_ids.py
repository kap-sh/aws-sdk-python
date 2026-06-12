"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AccountIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.account_id

AccountIds: TypeAlias = list["aws_sdk_compute_optimizer.types.account_id.AccountId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AccountIds:
    return list(data)
