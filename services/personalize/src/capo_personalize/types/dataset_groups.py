"""Generated from Smithy shape ``com.amazonaws.personalize#DatasetGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.dataset_group_summary

DatasetGroups: TypeAlias = list[
    "capo_personalize.types.dataset_group_summary.DatasetGroupSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetGroups) -> list:
    import capo_personalize.types.dataset_group_summary

    out: list = []
    for item in value:
        out.append(
            capo_personalize.types.dataset_group_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DatasetGroups:
    import capo_personalize.types.dataset_group_summary

    out: DatasetGroups = []
    for item in data:
        out.append(
            capo_personalize.types.dataset_group_summary.deserialize_aws_json_1_1(item)
        )
    return out
