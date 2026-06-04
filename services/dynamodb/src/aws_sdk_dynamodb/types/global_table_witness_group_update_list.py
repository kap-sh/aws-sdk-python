"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableWitnessGroupUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.global_table_witness_group_update

GlobalTableWitnessGroupUpdateList: TypeAlias = list[
    "aws_sdk_dynamodb.types.global_table_witness_group_update.GlobalTableWitnessGroupUpdate"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalTableWitnessGroupUpdateList) -> list:
    import aws_sdk_dynamodb.types.global_table_witness_group_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb.types.global_table_witness_group_update.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> GlobalTableWitnessGroupUpdateList:
    import aws_sdk_dynamodb.types.global_table_witness_group_update

    out: GlobalTableWitnessGroupUpdateList = []
    for item in data:
        out.append(
            aws_sdk_dynamodb.types.global_table_witness_group_update.deserialize_aws_json_1_0(
                item
            )
        )
    return out
