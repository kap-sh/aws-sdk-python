"""Generated from Smithy shape ``com.amazonaws.mturk#CustomerIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mturk.types.customer_id

CustomerIdList: TypeAlias = list["capo_mturk.types.customer_id.CustomerId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CustomerIdList:
    return list(data)
