"""Generated from Smithy shape ``com.amazonaws.batch#FrontOfQuotaSharesDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.front_of_quota_shares_job_summary_map
    import aws_sdk_batch.types.long


class FrontOfQuotaSharesDetail(TypedDict, closed=True):
    quota_shares: NotRequired[
        "aws_sdk_batch.types.front_of_quota_shares_job_summary_map.FrontOfQuotaSharesJobSummaryMap"
    ]
    """<p>Contains a list of the first <code>RUNNABLE</code> job in each named quota share.</p>"""
    last_updated_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the first <code>RUNNABLE</code> job per quota share were all last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrontOfQuotaSharesDetail) -> dict:
    out: dict = {}
    if "quota_shares" in value:
        import aws_sdk_batch.types.front_of_quota_shares_job_summary_map

        out["quotaShares"] = (
            aws_sdk_batch.types.front_of_quota_shares_job_summary_map.serialize_json(
                value["quota_shares"]
            )
        )
    if "last_updated_at" in value:
        out["lastUpdatedAt"] = value["last_updated_at"]
    return out


def deserialize_json(data: dict) -> FrontOfQuotaSharesDetail:
    out: FrontOfQuotaSharesDetail = {}  # type: ignore[typeddict-item]
    if "quotaShares" in data:
        import aws_sdk_batch.types.front_of_quota_shares_job_summary_map

        out["quota_shares"] = (
            aws_sdk_batch.types.front_of_quota_shares_job_summary_map.deserialize_json(
                data["quotaShares"]
            )
        )
    if "lastUpdatedAt" in data:
        out["last_updated_at"] = data["lastUpdatedAt"]
    return out
