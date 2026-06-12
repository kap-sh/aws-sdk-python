"""Generated from Smithy shape ``com.amazonaws.devicefarm#OfferingTransactions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.offering_transaction

OfferingTransactions: TypeAlias = list[
    "aws_sdk_device_farm.types.offering_transaction.OfferingTransaction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OfferingTransactions) -> list:
    import aws_sdk_device_farm.types.offering_transaction

    out: list = []
    for item in value:
        out.append(
            aws_sdk_device_farm.types.offering_transaction.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OfferingTransactions:
    import aws_sdk_device_farm.types.offering_transaction

    out: OfferingTransactions = []
    for item in data:
        out.append(
            aws_sdk_device_farm.types.offering_transaction.deserialize_aws_json_1_1(
                item
            )
        )
    return out
