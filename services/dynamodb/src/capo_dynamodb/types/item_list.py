"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_map

ItemList: TypeAlias = list["capo_dynamodb.types.attribute_map.AttributeMap"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ItemList) -> list:
    import capo_dynamodb.types.attribute_map

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.attribute_map.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ItemList:
    import capo_dynamodb.types.attribute_map

    out: ItemList = []
    for item in data:
        out.append(capo_dynamodb.types.attribute_map.deserialize_aws_json_1_0(item))
    return out
