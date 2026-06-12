"""Generated from Smithy shape ``com.amazonaws.datazone#AccountPoolSummaries``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_datazone.types.account_pool_summary

AccountPoolSummaries: TypeAlias = list["aws_sdk_datazone.types.account_pool_summary.AccountPoolSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountPoolSummaries) -> list:
    import aws_sdk_datazone.types.account_pool_summary
    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.account_pool_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountPoolSummaries:
    import aws_sdk_datazone.types.account_pool_summary
    out: AccountPoolSummaries = []
    for item in data:
        out.append(aws_sdk_datazone.types.account_pool_summary.deserialize_json(item))
    return out