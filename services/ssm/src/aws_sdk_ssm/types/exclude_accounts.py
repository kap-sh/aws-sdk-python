"""Generated from Smithy shape ``com.amazonaws.ssm#ExcludeAccounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.exclude_account

ExcludeAccounts: TypeAlias = list["aws_sdk_ssm.types.exclude_account.ExcludeAccount"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExcludeAccounts) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ExcludeAccounts:
    return list(data)
