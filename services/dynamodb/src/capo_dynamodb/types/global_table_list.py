"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.global_table

GlobalTableList: TypeAlias = list["capo_dynamodb.types.global_table.GlobalTable"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalTableList) -> list:
    import capo_dynamodb.types.global_table

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.global_table.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> GlobalTableList:
    import capo_dynamodb.types.global_table

    out: GlobalTableList = []
    for item in data:
        out.append(capo_dynamodb.types.global_table.deserialize_aws_json_1_0(item))
    return out
