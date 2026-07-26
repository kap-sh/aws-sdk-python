"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactWriteItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.transact_write_item

TransactWriteItemList: TypeAlias = list[
    "capo_dynamodb.types.transact_write_item.TransactWriteItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransactWriteItemList) -> list:
    import capo_dynamodb.types.transact_write_item

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.transact_write_item.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> TransactWriteItemList:
    import capo_dynamodb.types.transact_write_item

    out: TransactWriteItemList = []
    for item in data:
        out.append(
            capo_dynamodb.types.transact_write_item.deserialize_aws_json_1_0(item)
        )
    return out
