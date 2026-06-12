"""Generated from Smithy shape ``com.amazonaws.forecast#DatasetGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.dataset_group_summary

DatasetGroups: TypeAlias = list[
    "aws_sdk_forecast.types.dataset_group_summary.DatasetGroupSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetGroups) -> list:
    import aws_sdk_forecast.types.dataset_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_forecast.types.dataset_group_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DatasetGroups:
    import aws_sdk_forecast.types.dataset_group_summary

    out: DatasetGroups = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.dataset_group_summary.deserialize_aws_json_1_1(item)
        )
    return out
