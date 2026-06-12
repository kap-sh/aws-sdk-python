"""Generated from Smithy shape ``com.amazonaws.invoicing#BillSourceAccountList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_invoicing.types.account_id_string

BillSourceAccountList: TypeAlias = list["aws_sdk_invoicing.types.account_id_string.AccountIdString"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillSourceAccountList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> BillSourceAccountList:
    return list(data)