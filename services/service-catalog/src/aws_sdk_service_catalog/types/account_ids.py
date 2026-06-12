"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AccountIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.account_id

AccountIds: TypeAlias = list["aws_sdk_service_catalog.types.account_id.AccountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AccountIds:
    return list(data)
