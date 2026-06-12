"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DatasetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.dataset_summary

DatasetSummaries: TypeAlias = list[
    "aws_sdk_lookoutequipment.types.dataset_summary.DatasetSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatasetSummaries) -> list:
    import aws_sdk_lookoutequipment.types.dataset_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lookoutequipment.types.dataset_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DatasetSummaries:
    import aws_sdk_lookoutequipment.types.dataset_summary

    out: DatasetSummaries = []
    for item in data:
        out.append(
            aws_sdk_lookoutequipment.types.dataset_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
