"""Generated from Smithy shape ``com.amazonaws.batch#FrontOfQuotaShareJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.front_of_quota_share_job_summary

FrontOfQuotaShareJobSummaryList: TypeAlias = list[
    "capo_batch.types.front_of_quota_share_job_summary.FrontOfQuotaShareJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FrontOfQuotaShareJobSummaryList) -> list:
    import capo_batch.types.front_of_quota_share_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_batch.types.front_of_quota_share_job_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FrontOfQuotaShareJobSummaryList:
    import capo_batch.types.front_of_quota_share_job_summary

    out: FrontOfQuotaShareJobSummaryList = []
    for item in data:
        out.append(
            capo_batch.types.front_of_quota_share_job_summary.deserialize_json(item)
        )
    return out
