"""Generated from Smithy shape ``com.amazonaws.invoicing#RuleAccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.account_id_string

RuleAccountIdList: TypeAlias = list[
    "aws_sdk_invoicing.types.account_id_string.AccountIdString"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleAccountIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> RuleAccountIdList:
    return list(data)
