"""Generated from Smithy shape ``com.amazonaws.batch#FrontOfQuotaShareJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.front_of_quota_share_job_summary

FrontOfQuotaShareJobSummaryList: TypeAlias = list[
    "aws_sdk_batch.types.front_of_quota_share_job_summary.FrontOfQuotaShareJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FrontOfQuotaShareJobSummaryList) -> list:
    import aws_sdk_batch.types.front_of_quota_share_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_batch.types.front_of_quota_share_job_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FrontOfQuotaShareJobSummaryList:
    import aws_sdk_batch.types.front_of_quota_share_job_summary

    out: FrontOfQuotaShareJobSummaryList = []
    for item in data:
        out.append(
            aws_sdk_batch.types.front_of_quota_share_job_summary.deserialize_json(item)
        )
    return out
