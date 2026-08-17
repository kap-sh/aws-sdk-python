"""Generated from Smithy shape ``com.amazonaws.dynamodb#KeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.key

KeyList: TypeAlias = list["capo_dynamodb.types.key.Key"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyList) -> list:
    import capo_dynamodb.types.key

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.key.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> KeyList:
    import capo_dynamodb.types.key

    out: KeyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_dynamodb.types.key.deserialize_aws_json_1_0(item))
    return out
