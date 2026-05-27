"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableWitnessDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.global_table_witness_description

GlobalTableWitnessDescriptionList: TypeAlias = list[
    "aws_sdk_dynamodb.types.global_table_witness_description.GlobalTableWitnessDescription"
]
