"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListLabelingJobsForWorkteamSortByOptions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ListLabelingJobsForWorkteamSortByOptions: TypeAlias = Literal["CreationTime",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CreationTime",))


def serialize_aws_json_1_1(value: ListLabelingJobsForWorkteamSortByOptions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListLabelingJobsForWorkteamSortByOptions:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListLabelingJobsForWorkteamSortByOptions value: {data!r}"
        )
    return cast(ListLabelingJobsForWorkteamSortByOptions, data)
