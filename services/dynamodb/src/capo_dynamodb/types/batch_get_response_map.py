"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchGetResponseMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.item_list
    import capo_dynamodb.types.table_arn

BatchGetResponseMap: TypeAlias = dict[
    "capo_dynamodb.types.table_arn.TableArn", "capo_dynamodb.types.item_list.ItemList"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: BatchGetResponseMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_dynamodb.types.item_list

        out[key] = capo_dynamodb.types.item_list.serialize_aws_json_1_0(value)
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetResponseMap:
    out: BatchGetResponseMap = {}
    for key, value in data.items():
        import capo_dynamodb.types.item_list

        out[key] = capo_dynamodb.types.item_list.deserialize_aws_json_1_0(value)
    return out
