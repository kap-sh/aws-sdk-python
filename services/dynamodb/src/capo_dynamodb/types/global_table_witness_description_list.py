"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableWitnessDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.global_table_witness_description

GlobalTableWitnessDescriptionList: TypeAlias = list[
    "capo_dynamodb.types.global_table_witness_description.GlobalTableWitnessDescription"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalTableWitnessDescriptionList) -> list:
    import capo_dynamodb.types.global_table_witness_description

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.global_table_witness_description.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> GlobalTableWitnessDescriptionList:
    import capo_dynamodb.types.global_table_witness_description

    out: GlobalTableWitnessDescriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.global_table_witness_description.deserialize_aws_json_1_0(
                item
            )
        )
    return out
