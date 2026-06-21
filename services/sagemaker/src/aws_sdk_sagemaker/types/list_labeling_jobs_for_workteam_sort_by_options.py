"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListLabelingJobsForWorkteamSortByOptions``."""

from typing import Literal, TypeAlias, cast

ListLabelingJobsForWorkteamSortByOptions: TypeAlias = Literal["CreationTime",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLabelingJobsForWorkteamSortByOptions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListLabelingJobsForWorkteamSortByOptions:
    return cast(ListLabelingJobsForWorkteamSortByOptions, data)
