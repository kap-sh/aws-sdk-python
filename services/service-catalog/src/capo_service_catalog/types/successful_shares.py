"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SuccessfulShares``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.account_id

SuccessfulShares: TypeAlias = list["capo_service_catalog.types.account_id.AccountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuccessfulShares) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SuccessfulShares:
    return list(data)
