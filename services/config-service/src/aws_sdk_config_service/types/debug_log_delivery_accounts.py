"""Generated from Smithy shape ``com.amazonaws.configservice#DebugLogDeliveryAccounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.account_id

DebugLogDeliveryAccounts: TypeAlias = list[
    "aws_sdk_config_service.types.account_id.AccountId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DebugLogDeliveryAccounts) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DebugLogDeliveryAccounts:
    return list(data)
