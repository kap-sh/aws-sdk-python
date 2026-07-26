"""Generated from Smithy shape ``com.amazonaws.configservice#ExcludedAccounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.account_id

ExcludedAccounts: TypeAlias = list["capo_config_service.types.account_id.AccountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExcludedAccounts) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ExcludedAccounts:
    return list(data)
