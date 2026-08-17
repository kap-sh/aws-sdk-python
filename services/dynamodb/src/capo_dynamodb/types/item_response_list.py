"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.item_response

ItemResponseList: TypeAlias = list["capo_dynamodb.types.item_response.ItemResponse"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ItemResponseList) -> list:
    import capo_dynamodb.types.item_response

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.item_response.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ItemResponseList:
    import capo_dynamodb.types.item_response

    out: ItemResponseList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_dynamodb.types.item_response.deserialize_aws_json_1_0(item))
    return out
