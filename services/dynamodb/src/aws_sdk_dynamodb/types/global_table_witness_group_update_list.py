"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableWitnessGroupUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.global_table_witness_group_update

GlobalTableWitnessGroupUpdateList: TypeAlias = list[
    "aws_sdk_dynamodb.types.global_table_witness_group_update.GlobalTableWitnessGroupUpdate"
]
