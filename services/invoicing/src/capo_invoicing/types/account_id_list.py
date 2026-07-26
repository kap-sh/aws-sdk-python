"""Generated from Smithy shape ``com.amazonaws.invoicing#AccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_invoicing.types.account_id_string

AccountIdList: TypeAlias = list[
    "capo_invoicing.types.account_id_string.AccountIdString"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AccountIdList:
    return list(data)
