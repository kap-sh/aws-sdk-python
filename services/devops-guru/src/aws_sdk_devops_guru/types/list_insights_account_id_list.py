"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListInsightsAccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.aws_account_id

ListInsightsAccountIdList: TypeAlias = list[
    "aws_sdk_devops_guru.types.aws_account_id.AwsAccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListInsightsAccountIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ListInsightsAccountIdList:
    return list(data)
