"""Generated from Smithy shape ``com.amazonaws.transfer#AddressAllocationIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transfer.types.address_allocation_id

AddressAllocationIds: TypeAlias = list[
    "aws_sdk_transfer.types.address_allocation_id.AddressAllocationId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddressAllocationIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AddressAllocationIds:
    return list(data)
