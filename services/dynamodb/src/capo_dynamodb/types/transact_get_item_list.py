"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactGetItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.transact_get_item

TransactGetItemList: TypeAlias = list[
    "capo_dynamodb.types.transact_get_item.TransactGetItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransactGetItemList) -> list:
    import capo_dynamodb.types.transact_get_item

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.transact_get_item.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> TransactGetItemList:
    import capo_dynamodb.types.transact_get_item

    out: TransactGetItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_dynamodb.types.transact_get_item.deserialize_aws_json_1_0(item))
    return out
