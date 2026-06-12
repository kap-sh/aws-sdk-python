"""Generated from Smithy shape ``com.amazonaws.batch#FrontOfQuotaSharesJobSummaryMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.front_of_quota_share_job_summary_list
    import aws_sdk_batch.types.string

FrontOfQuotaSharesJobSummaryMap: TypeAlias = dict[
    "aws_sdk_batch.types.string.String",
    "aws_sdk_batch.types.front_of_quota_share_job_summary_list.FrontOfQuotaShareJobSummaryList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FrontOfQuotaSharesJobSummaryMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_batch.types.front_of_quota_share_job_summary_list

        out[key] = (
            aws_sdk_batch.types.front_of_quota_share_job_summary_list.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> FrontOfQuotaSharesJobSummaryMap:
    out: FrontOfQuotaSharesJobSummaryMap = {}
    for key, value in data.items():
        import aws_sdk_batch.types.front_of_quota_share_job_summary_list

        out[key] = (
            aws_sdk_batch.types.front_of_quota_share_job_summary_list.deserialize_json(
                value
            )
        )
    return out
